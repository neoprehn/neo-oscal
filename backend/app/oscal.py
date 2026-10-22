"""Minimale OSCAL-Katalog-Modelle (Schicht 1 des OSCAL-Modells).

Es werden nur die Felder modelliert, die das Tool braucht; alles Weitere
bleibt beim Einlesen erhalten (extra="allow"), damit ein späterer Export
verlustfrei bleibt.
"""
from __future__ import annotations

import json
from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field


class _Base(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class Part(_Base):
    id: str | None = None
    name: str
    prose: str | None = None
    parts: list[Part] = []


class Control(_Base):
    id: str
    title: str
    cls: str | None = Field(default=None, alias="class")
    parts: list[Part] = []
    controls: list[Control] = []  # Control-Enhancements


class Group(_Base):
    id: str | None = None
    title: str
    controls: list[Control] = []
    groups: list[Group] = []


class Catalog(_Base):
    uuid: str
    metadata: dict
    groups: list[Group] = []
    controls: list[Control] = []

    @property
    def title(self) -> str:
        return self.metadata.get("title", "")

    def iter_controls(self):
        """Alle Controls inkl. Enhancements, flach und in Dokumentreihenfolge."""

        def walk_control(c: Control):
            yield c
            for sub in c.controls:
                yield from walk_control(sub)

        def walk_group(g: Group):
            for c in g.controls:
                yield from walk_control(c)
            for sub in g.groups:
                yield from walk_group(sub)

        for c in self.controls:
            yield from walk_control(c)
        for g in self.groups:
            yield from walk_group(g)


def load_catalog(path: Path) -> Catalog:
    """Liest eine OSCAL-JSON-Datei, entweder mit {"catalog": ...} als Wurzel oder direkt."""
    data = json.loads(path.read_text(encoding="utf-8"))
    return Catalog.model_validate(data.get("catalog", data))
