from dataclasses import dataclass, field
from types.types import Pair
from typing import Optional

# ============================================================================
# PERSONAL INFO MODEL
# ============================================================================


@dataclass
class PersonalInfo:
    """
    Basic personal information
    """

    name: str
    lastname: str
    email: str
    phone: str
    links: list[Pair[str, str]] = field(default_factory=list)


# ============================================================================
# EXPERIENCE AND EDUCATION MODELS
# ============================================================================


@dataclass
class Experience:
    """
    Work experience
    """

    position: str
    company: str
    period: str
    tasks: list[str] = field(default_factory=list)
    skills: list[str] = field(default_factory=list)


@dataclass
class Education:
    """
    Academic education
    """

    degree: str
    institution: str
    period: Pair[int, int]
    description: Optional[str] = None


# ============================================================================
# SKILLS AND PROJECTS MODELS
# ============================================================================


@dataclass
class SkillCategory:
    """
    Skill category
    """

    category: str
    items: list[str] = field(default_factory=list)


@dataclass
class Project:
    """
    Professional or personal projects
    """

    name: str
    description: str
    technologies: list[str] = field(default_factory=list)
    repo: Optional[str] = None


# ============================================================================
# CERTIFICATIONS AND REFERENCES MODELS
# ============================================================================


@dataclass
class Reference:
    """
    Professional references
    """

    name: str
    position: Optional[str] = None
    company: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    note: Optional[str] = None


# ============================================================================
# MAIN PERSON MODEL
# ============================================================================


@dataclass
class Person:
    """
    Main model representation of all the data of a person needed for a CV
    """

    personal_info: PersonalInfo
    summary: str
    experiences: list[Experience] = field(default_factory=list)
    education: list[Education] = field(default_factory=list)
    skill_categories: list[SkillCategory] = field(default_factory=list)
    projects: list[Project] = field(default_factory=list)
    certifications: list[str] = field(default_factory=list)
    references: list[Reference] = field(default_factory=list)
