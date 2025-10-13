import json
import re
from dataclasses import asdict, is_dataclass

from src.domain.entities.person import (
    Education,
    Experience,
    Person,
    PersonalInfo,
    Project,
    Reference,
    SkillCategory,
)
from src.infraestructure.config.paths import PERSON_STORAGE


class PersonJsonStorage:

    @staticmethod
    def __sanitize_filename(name: str) -> str:
        """Convierte un string a un nombre de archivo seguro."""
        return re.sub(r"[^a-zA-Z0-9_-]+", "_", name.strip().lower())

    @staticmethod
    def save_person(person: Person):
        """Guarda un objeto Person como JSON."""
        if not is_dataclass(person):
            raise TypeError("Expected a dataclass instance.")

        safe_name = PersonJsonStorage.__sanitize_filename(
            person.personal_info.name
        )
        file_name = (PERSON_STORAGE / safe_name).with_suffix(".json")

        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(asdict(person), f, indent=2, ensure_ascii=False)

    @staticmethod
    def load_person(name: str) -> Person | None:
        """Carga una persona si existe, o None."""
        safe_name = PersonJsonStorage.__sanitize_filename(name)
        file_name = (PERSON_STORAGE / safe_name).with_suffix(".json")

        if not file_name.exists():
            return None

        with open(file_name, "r", encoding="utf-8") as f:
            data = json.load(f)

        return Person(
            personal_info=PersonalInfo(**data["personal_info"]),
            summary=data.get("summary", ""),
            experiences=[Experience(**e) for e in data.get("experiences", [])],
            education=[Education(**e) for e in data.get("education", [])],
            skill_categories=[
                SkillCategory(**c) for c in data.get("skill_categories", [])
            ],
            projects=[Project(**p) for p in data.get("projects", [])],
            certifications=data.get("certifications", []),
            references=[Reference(**r) for r in data.get("references", [])],
        )
