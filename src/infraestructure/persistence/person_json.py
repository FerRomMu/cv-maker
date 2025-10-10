import json
import re
from dataclasses import asdict, is_dataclass

from src.domain.entities.person import Person
from src.infraestructure.config.paths import PERSON_STORAGE


def sanitize_filename(name: str) -> str:
    """Convierte un string a un nombre de archivo seguro."""
    return re.sub(r"[^a-zA-Z0-9_-]+", "_", name.strip().lower())


def save_person(person: Person):
    """Guarda un objeto Person como JSON."""
    if not is_dataclass(person):
        raise TypeError("Expected a dataclass instance.")

    safe_name = sanitize_filename(person.personal_info.name)
    file_name = (PERSON_STORAGE / safe_name).with_suffix(".json")

    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(asdict(person), f, indent=2, ensure_ascii=False)


def load_person(name: str) -> Person | None:
    """Carga una persona si existe, o None."""
    safe_name = sanitize_filename(name)
    file_name = (PERSON_STORAGE / safe_name).with_suffix(".json")

    if not file_name.exists():
        return None

    with open(file_name, "r", encoding="utf-8") as f:
        data = json.load(f)
    return Person(**data)
