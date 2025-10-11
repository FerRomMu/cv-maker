from dataclasses import dataclass

from src.domain.entities.person import Person
from src.domain.enums import Lang, Section


@dataclass
class ResumeTemplate:
    template_name: str
    sections: list[Section]
    lang: Lang


@dataclass
class Resume:
    template: ResumeTemplate
    person: Person
