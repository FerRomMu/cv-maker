from src.aplication.formatters import ResumeFormatter
from src.domain.entities.person import (
    Education,
    Experience,
    Person,
    PersonalInfo,
    Project,
    Reference,
    SkillCategory,
)
from src.domain.entities.resume import Resume, ResumeTemplate
from src.domain.enums import Lang, Section
from src.infraestructure.config.paths import OUTPUT
from src.infraestructure.jinja_renderer import JinjaRenderer

# ---------------------------
# Datos de ejemplo para el CV
# ---------------------------
user: Person = Person(
    personal_info=PersonalInfo(
        name="Fernando",
        lastname="Romero Muñoz",
        email="fernando@example.com",
        phone="+54 9 11 5555-5555",
        links=[
            ("LinkedIn", "https://linkedin.com/in/fernandomunoz"),
            ("GitHub", "https://github.com/fernandomunoz"),
        ],
    ),
    summary=(
        "Software developer specialized in Python and Kotlin, with experience "
        "in backend architectures, AI integration, and scalable modular design."
    ),
    experiences=[
        Experience(
            position="Backend Developer",
            company="TechCorp",
            period="2021 - Present",
            tasks=[
                "Develop RESTful APIs using FastAPI",
                "Integrate LLM-based services for document parsing",
                "Manage CI/CD pipelines using GitHub Actions",
            ],
            skills=["Python", "FastAPI", "Docker", "PostgreSQL"],
        ),
        Experience(
            position="Software Engineer",
            company="DataWorks",
            period="2019 - 2021",
            tasks=[
                "Built internal tools for data processing with pandas",
                "Optimized database queries and ETL pipelines",
            ],
            skills=["pandas", "SQLAlchemy", "ETL"],
        ),
    ],
    education=[
        Education(
            degree="Bachelor in Computer Science",
            institution="Universidad de Buenos Aires",
            period=(2014, 2019),
            description="Focus on software architecture and distributed systems.",
        ),
    ],
    skill_categories=[
        SkillCategory(
            category="Programming Languages",
            items=["Python", "Kotlin", "JavaScript"],
        ),
        SkillCategory(
            category="Frameworks", items=["FastAPI", "Flask", "React"]
        ),
        SkillCategory(category="Tools", items=["Docker", "Git", "CI/CD"]),
    ],
    projects=[
        Project(
            name="gitllm",
            description="Open-source tool for generating commit messages using LLMs.",
            technologies=["Python", "Git", "LLM APIs"],
            repo="https://github.com/fernandomunoz/gitllm",
        ),
        Project(
            name="KanbanApp",
            description="Lightweight Kanban board built with Jetpack Compose.",
            technologies=["Kotlin", "Jetpack Compose"],
        ),
    ],
    certifications=[
        "Azure AI Fundamentals",
        "Google Cloud Associate Engineer",
    ],
    references=[
        Reference(
            name="Laura Gómez",
            position="CTO",
            company="TechCorp",
            email="laura.gomez@techcorp.com",
            phone="+54 9 11 4444-4444",
            note="Direct manager during backend development projects.",
        ),
        Reference(
            name="Martín Pérez",
            position="Team Lead",
            company="DataWorks",
            email="martin.perez@dataworks.com",
        ),
    ],
)

template = ResumeTemplate(
    template_name="base",
    sections=[
        Section.PERSONAL_INFO,
        Section.SUMMARY,
        Section.EXPERIENCES,
        Section.EDUCATION,
        Section.SKILLS,
        Section.PROJECTS,
        Section.CERTIFICATIONS,
        Section.REFERENCES,
    ],
    lang=Lang.ES,
)

resume = Resume(user, template)

formatted_data = ResumeFormatter.format(resume)
rendered_data = JinjaRenderer.render(formatted_data)

with open(OUTPUT / f"{user.full_name()}.tex", "w", encoding="utf-8") as f:
    f.write(rendered_data)

print("Archivo output.tex generado correctamente.")
