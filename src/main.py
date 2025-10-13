from src.aplication.formatters import ResumeFormatter
from src.domain.entities.person import Person
from src.domain.entities.resume import Resume, ResumeTemplate
from src.domain.enums import Lang, Section
from src.infraestructure.config.paths import OUTPUT
from src.infraestructure.jinja_renderer import JinjaRenderer
from src.infraestructure.persistence.json import PersonJsonStorage

# ---------------------------
# Datos de ejemplo para el CV
# ---------------------------
user: Person = PersonJsonStorage.load_person("fernando_mario")

template = ResumeTemplate(
    template_name="base",
    sections=[
        Section.PERSONAL_INFO,
        Section.SUMMARY,
        Section.EXPERIENCES,
        Section.EDUCATION,
        Section.SKILL_CATEGORIES,
    ],
    lang=Lang.ES,
)

resume = Resume(template=template, person=user)

formatted_data = ResumeFormatter.format(resume)
rendered_data = JinjaRenderer.render(
    resume.template.template_name, formatted_data
)

with open(OUTPUT / f"{user.full_name()}.tex", "w", encoding="utf-8") as f:
    f.write(rendered_data)

print("Archivo output.tex generado correctamente.")
