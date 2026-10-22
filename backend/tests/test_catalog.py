import json

from fastapi.testclient import TestClient

from app import main
from app.oscal import load_catalog

SAMPLE = {
    "catalog": {
        "uuid": "00000000-0000-4000-8000-000000000001",
        "metadata": {"title": "Test-Katalog"},
        "groups": [
            {
                "id": "ac",
                "title": "Access Control",
                "controls": [
                    {
                        "id": "ac-1",
                        "title": "Policy and Procedures",
                        "controls": [{"id": "ac-1.1", "title": "Enhancement"}],
                    }
                ],
            }
        ],
    }
}


def test_iter_controls_includes_enhancements(tmp_path):
    p = tmp_path / "x_catalog.json"
    p.write_text(json.dumps(SAMPLE), encoding="utf-8")
    ids = [c.id for c in load_catalog(p).iter_controls()]
    assert ids == ["ac-1", "ac-1.1"]


def test_api_search(tmp_path, monkeypatch):
    (tmp_path / "x_catalog.json").write_text(json.dumps(SAMPLE), encoding="utf-8")
    monkeypatch.setattr(main, "CONTENT_DIR", tmp_path)
    with TestClient(main.app) as client:
        assert client.get("/api/catalogs").json()[0]["controls"] == 2
        hits = client.get("/api/catalogs/x_catalog/controls", params={"q": "policy"}).json()
        assert [h["id"] for h in hits] == ["ac-1"]
        assert client.get("/api/catalogs/nope/controls").status_code == 404
