from pathlib import Path

ROOT = Path(__file__).parent.parent

DATA = ROOT / ".app_data"
OUTPUT = ROOT / "outputs"
RESOURCES = ROOT / "resources"

TEMPLATES = RESOURCES / "templates"

PERSON_STORAGE = DATA / "person"

dirs = [DATA, OUTPUT, RESOURCES, TEMPLATES, PERSON_STORAGE]
for dirr in dirs:
    dirr.mkdir(parents=True, exist_ok=True)
