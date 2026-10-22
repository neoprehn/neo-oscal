import os
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException, Query

from .oscal import Catalog, load_catalog

CONTENT_DIR = Path(os.environ.get("OSCAL_CONTENT_DIR", Path(__file__).parents[2] / "data" / "content"))

_catalogs: dict[str, Catalog] = {}


def _load_all() -> None:
    _catalogs.clear()
    for path in sorted(CONTENT_DIR.glob("*catalog*.json")):
        _catalogs[path.stem] = load_catalog(path)


@asynccontextmanager
async def lifespan(_: FastAPI):
    _load_all()
    yield


app = FastAPI(title="neo-oscal", version="0.1.0", lifespan=lifespan)


@app.get("/api/health")
def health() -> dict:
    return {"status": "ok", "catalogs": len(_catalogs)}


@app.get("/api/catalogs")
def list_catalogs() -> list[dict]:
    return [
        {"id": cid, "title": c.title, "controls": sum(1 for _ in c.iter_controls())}
        for cid, c in _catalogs.items()
    ]


@app.get("/api/catalogs/{catalog_id}/controls")
def search_controls(catalog_id: str, q: str = "", limit: int = Query(50, le=500)) -> list[dict]:
    catalog = _catalogs.get(catalog_id)
    if catalog is None:
        raise HTTPException(404, "Katalog nicht gefunden")
    needle = q.lower()
    hits = [
        {"id": c.id, "title": c.title}
        for c in catalog.iter_controls()
        if not needle or needle in c.id.lower() or needle in c.title.lower()
    ]
    return hits[:limit]
