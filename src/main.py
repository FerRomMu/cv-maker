from pathlib import Path

from jinja2 import Environment, FileSystemLoader

# ---------------------------
# Paths
# ---------------------------

base_path = Path.cwd()
output_path = base_path / "outputs"
template_path = Path.cwd() / "src" / "templates"


# ---------------------------
# Filtro para escapear caracteres especiales de LaTeX
# ---------------------------
def latex_escape(s: str) -> str:
    if s is None:
        return ""
    s = str(s)
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    for k, v in replacements.items():
        s = s.replace(k, v)
    return s


# ---------------------------
# Cargar plantilla
# ---------------------------
env = Environment(loader=FileSystemLoader(template_path), autoescape=False)
env.filters["latex_escape"] = latex_escape
template = env.get_template("base.tex.jinja2")  # tu plantilla .jinja

# ---------------------------
# Datos de ejemplo para el CV
# ---------------------------
data = {
    "person": {
        "name": "Lorem",
        "lastname": "Ipsum Dolor",
        "email": "lorem@ipsum.com",
        "linkedin": "linkedin.com/in/loremipsum",
        "phone": "(11) 1234-5678",
    },
    "titles": {
        "SUMMARY": "RESUMEN",
        "EXPERIENCE": "EXPERIENCIA",
        "EDUCATION": "EDUCACIÓN",
        "SKILLS": "HABILIDADES",
        "PROJECTS": "PROYECTOS",
        "CERTIFICATIONS": "CERTIFICACIONES",
        "REFERENCES": "REFERENCIAS",
    },
    "labels": {
        "SKILLS": "Habilidades",
        "DESCRIPTION": "Descripción",
        "TECHNOLOGIES": "Tecnologías",
        "REPOSITORY": "Repositorio",
    },
    "summary": (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        " Sed do eiusmod tempor incididunt ut labore"
        " et dolore magna aliqua."
    ),
    "experiencia": [
        {
            "position": "Senior Backend Engineer",
            "company": "Fictional Corp S.A.",
            "period": "Enero 2023 - Presente",
            "tasks": [
                "Desarrollo de microservicios con tecnologías de vanguardia.",
                "Implementación de patrones de diseño escalables y robustos.",
                (
                    "Optimización de rendimiento"
                    " y gestión de bases de datos NoSQL."
                ),
            ],
            "skills": ["Python", "Django", "PostgreSQL"],
        },
        {
            "position": "Frontend Developer",
            "company": "Dummy Solutions",
            "period": "Marzo 2021 - Diciembre 2022",
            "tasks": [
                (
                    "Creación de interfaces de usuario"
                    " interactivas con librería X."
                ),
                "Consumo de APIs RESTful y gestión de estado global.",
                "Colaboración en metodologías ágiles y CI/CD.",
            ],
            "skills": ["React", "TypeScript", "Redux", "Jest"],
        },
    ],
    "education": [
        {
            "degree": "Licenciatura en Tecnología",
            "institution": "Instituto Central",
            "period": "2018 - 2022",
        }
    ],
    "skills": {
        "Lenguajes de Programación": [
            "Ficticio Uno",
            "Ficticio Dos",
            "Ficticio Tres",
            "Ficticio Cuatro",
        ],
        "Frameworks y Librerías": [
            "Framework X",
            "Librería Y",
            "Herramienta Z",
            "Tecnología W",
        ],
        "Bases de Datos": ["BD Tipo A", "BD Tipo B", "BD Tipo C"],
        "Cloud y DevOps": [
            "Cloud Ficticia",
            "Contenedores",
            "Orquestador",
            "Flujo CI/CD",
        ],
        "Herramientas": ["Herramienta 1", "Herramienta 2", "Herramienta 3"],
    },
    "projects": [
        {
            "name": "Proyecto Ficticio Alpha",
            "description": (
                "Aplicación de prueba para demostración de arquitectura"
                " hexagonal."
            ),
            "technologies": ["Tecnología A", "Tecnología B", "Tecnología C"],
            "repo": "https://github.com/loremipsum/proyecto-ficticio",
        }
    ],
    "certifications": [
        "Certificación Ficticia Nivel Junior",
        "Curso Avanzado de Desarrollo XYZ",
    ],
    "references": [
        {
            "name": "Jane Doe",
            "position": "Manager",
            "company": "Fictional Corp S.A.",
            "note": "Supervisor de proyectos de desarrollo fullstack.",
            "email": "jane.doe@fictional.com",
            "phone": "(11) 9876-5432",
        }
    ],
}

# ---------------------------
# Renderizar plantilla y guardar .tex
# ---------------------------
rendered = template.render(**data)
with open(output_path / "output.tex", "w", encoding="utf-8") as f:
    f.write(rendered)

print("Archivo output.tex generado correctamente.")
