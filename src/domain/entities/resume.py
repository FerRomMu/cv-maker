from dataclasses import dataclass

from src.domain.entities.person import Person


@dataclass
class ResumeTemplate:
    template_name: str
    sections: list[str]


@dataclass
class Resume:
    template: ResumeTemplate
    person: Person
