"""Lädt den NIST-SP-800-53-Rev5-Katalog und die Baselines aus usnistgov/oscal-content."""
import urllib.request
from pathlib import Path

BASE = "https://raw.githubusercontent.com/usnistgov/oscal-content/main/nist.gov/SP800-53/rev5/json"
FILES = [
    "NIST_SP-800-53_rev5_catalog.json",
    "NIST_SP-800-53_rev5_LOW-baseline_profile.json",
    "NIST_SP-800-53_rev5_MODERATE-baseline_profile.json",
    "NIST_SP-800-53_rev5_HIGH-baseline_profile.json",
]
DEST = Path(__file__).parents[1] / "data" / "content"

DEST.mkdir(parents=True, exist_ok=True)
for name in FILES:
    print("lade", name)
    urllib.request.urlretrieve(f"{BASE}/{name}", DEST / name)
