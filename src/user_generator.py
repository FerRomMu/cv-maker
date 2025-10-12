from src.domain.entities.person import (
    Education,
    Experience,
    Person,
    PersonalInfo,
    Project,
    Reference,
    SkillCategory,
)
from src.infraestructure.persistence.json import PersonJsonStorage

# ---------------------------
# Datos de ejemplo a rellenar
# ---------------------------
user: Person = Person(
    personal_info=PersonalInfo(
        name="Nombre",
        lastname="Apellido",
        email="mail@example.com",
        phone="+54 9 11 5555-5555",
        links=[
            ("LinkedIn", "https://linkedin.com/in/profile"),
            ("GitHub", "https://github.com/profile"),
            ("Otro", "https://otro.com"),
        ],
    ),
    summary=("Your resume"),
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
            institution="Universidad Nacional de Quilmes",
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
            description="Open-source tool for generating cv.",
            technologies=["Python", "Git", "LLM APIs"],
            repo="https://github.com/FerRomMu/cv-maker",
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

PersonJsonStorage.save_person(user)
