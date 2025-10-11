from typing import Any

from src.domain.entities.person import (
    Education,
    Experience,
    Person,
    PersonalInfo,
    Project,
    Reference,
    SkillCategory,
)
from src.domain.entities.resume import Resume
from src.domain.enums import Lang, Section


class PersonFormatter:

    @staticmethod
    def __set_formatted_data(data: dict, section: Section, value: Any):
        if value is not None:
            data[section] = value

    # ----------------------------------------------------------------------
    # PERSONAL INFO
    # ----------------------------------------------------------------------
    @staticmethod
    def __format_info(info: PersonalInfo):
        return {
            "name": info.name,
            "lastname": info.lastname,
            "email": info.email,
            "phone": info.phone,
            "links": (
                [{"name": link[0], "url": link[1]} for link in info.links]
                if info.links
                else None
            ),
        }

    # ----------------------------------------------------------------------
    # EXPERIENCES
    # ----------------------------------------------------------------------
    @staticmethod
    def __format_experiencies(experiences: list[Experience]):
        if not experiences:
            return None
        return [
            {
                "position": exp.position,
                "company": exp.company,
                "period": exp.period,
                "tasks": exp.tasks if exp.tasks else None,
                "skills": exp.skills if exp.skills else None,
            }
            for exp in experiences
        ]

    # ----------------------------------------------------------------------
    # EDUCATION
    # ----------------------------------------------------------------------
    @staticmethod
    def __format_education(education: list[Education]):
        if not education:
            return None
        return [
            {
                "degree": edu.degree,
                "institution": edu.institution,
                "period": {
                    "start": edu.period[0],
                    "end": edu.period[1],
                },
                "description": edu.description,
            }
            for edu in education
        ]

    # ----------------------------------------------------------------------
    # SKILLS
    # ----------------------------------------------------------------------
    @staticmethod
    def __format_skills(skill_categories: list[SkillCategory]):
        if not skill_categories:
            return None
        return [
            {
                "category": cat.category,
                "items": cat.items if cat.items else None,
            }
            for cat in skill_categories
        ]

    # ----------------------------------------------------------------------
    # PROJECTS
    # ----------------------------------------------------------------------
    @staticmethod
    def __format_projects(projects: list[Project]):
        if not projects:
            return None
        return [
            {
                "name": proj.name,
                "description": proj.description,
                "technologies": (
                    proj.technologies if proj.technologies else None
                ),
                "repo": proj.repo,
            }
            for proj in projects
        ]

    # ----------------------------------------------------------------------
    # CERTIFICATIONS
    # ----------------------------------------------------------------------
    @staticmethod
    def __format_certifications(certifications: list[str]):
        return certifications if certifications else None

    # ----------------------------------------------------------------------
    # REFERENCES
    # ----------------------------------------------------------------------
    @staticmethod
    def __format_references(references: list[Reference]):
        if not references:
            return None
        return [
            {
                "name": ref.name,
                "position": ref.position,
                "company": ref.company,
                "email": ref.email,
                "phone": ref.phone,
                "note": ref.note,
            }
            for ref in references
        ]

    # ----------------------------------------------------------------------
    # MAIN FORMAT ENTRY POINT
    # ----------------------------------------------------------------------
    @staticmethod
    def format(person: Person) -> dict[Section, Any]:
        formatted_data = {}

        mappings = [
            (
                Section.PERSONAL_INFO,
                PersonFormatter.__format_info,
                person.personal_info,
            ),
            (Section.SUMMARY, lambda x: x if x else None, person.summary),
            (
                Section.EXPERIENCES,
                PersonFormatter.__format_experiencies,
                person.experiences,
            ),
            (
                Section.EDUCATION,
                PersonFormatter.__format_education,
                person.education,
            ),
            (
                Section.SKILL_CATEGORIES,
                PersonFormatter.__format_skills,
                person.skill_categories,
            ),
            (
                Section.PROJECTS,
                PersonFormatter.__format_projects,
                person.projects,
            ),
            (
                Section.CERTIFICATIONS,
                PersonFormatter.__format_certifications,
                person.certifications,
            ),
            (
                Section.REFERENCES,
                PersonFormatter.__format_references,
                person.references,
            ),
        ]

        for section, func, value in mappings:
            PersonFormatter.__set_formatted_data(
                formatted_data, section, func(value)
            )

        return formatted_data


class ResumeFormatter:

    @staticmethod
    def format(resume: Resume):
        formatted_data: dict[Section, Any] = {}

        formatted_person: dict[Section, Any] = PersonFormatter.format(
            resume.person
        )
        resume_sections: list[Section] = [
            section
            for section in resume.template.sections
            if section in formatted_person
        ]

        titles: dict[Section, str] = {}
        lang: Lang = resume.template.lang
        for section in resume_sections:
            titles[section] = section.to_str(lang)

        formatted_data["titles"] = titles
        formatted_data["person"] = {
            key: value
            for key, value in formatted_person.items()
            if key in titles
        }

        return formatted_data
