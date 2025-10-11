from enum import Enum


class Lang(Enum):
    ES = "es"
    EN = "en"


class Section(Enum):
    PERSONAL_INFO = "personal_info"
    SUMMARY = "summary"
    EXPERIENCES = "experiences"
    EDUCATION = "education"
    SKILL_CATEGORIES = "skill_categories"
    PROJECTS = "projects"
    CERTIFICATIONS = "certifications"
    REFERENCES = "references"

    __TRANSLATIONS = {
        "personal_info": {
            "en": "PERSONAL INFORMATION",
            "es": "INFORMACIÓN PERSONAL",
        },
        "summary": {"en": "SUMMARY", "es": "RESUMEN"},
        "experiences": {"en": "EXPERIENCE", "es": "EXPERIENCIA"},
        "education": {"en": "EDUCATION", "es": "EDUCACIÓN"},
        "skill_categories": {"en": "SKILLS", "es": "HABILIDADES"},
        "projects": {"en": "PROJECTS", "es": "PROYECTOS"},
        "certifications": {"en": "CERTIFICATIONS", "es": "CERTIFICACIONES"},
        "references": {"en": "REFERENCES", "es": "REFERENCIAS"},
    }

    def str_en(self) -> str:
        return self.__TRANSLATIONS[self.value]["en"]

    def str_es(self) -> str:
        return self.__TRANSLATIONS[self.value]["es"]

    def to_str(self, lang: Lang) -> str:
        match lang:
            case Lang.ES:
                return self.str_es()
            case Lang.EN:
                return self.str_en()
            case _:
                raise ValueError("No existe lenguaje dado.")
