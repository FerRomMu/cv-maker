from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from src.infraestructure.config.paths import TEMPLATES
from src.infraestructure.latex_filter import latex_escape


class JinjaRenderer:

    @staticmethod
    def __validate_template(name: str):
        template_path = TEMPLATES / name
        if template_path.exists():
            return name
        if template_path.with_suffix(".jinja2").exists():
            return template_path.with_suffix(".jinja2").name
        if template_path.with_suffix(".tex.jinja2").exists():
            return template_path.with_suffix(".tex.jinja2").name
        raise FileNotFoundError(
            f"Template '{name}' no encontrado en {TEMPLATES}"
        )

    @staticmethod
    def render(
        template_name: str, context: dict, template_dir: Path = TEMPLATES
    ) -> str:
        env = Environment(
            loader=FileSystemLoader(template_dir), autoescape=False
        )
        env.filters["latex_escape"] = latex_escape
        checked_name = JinjaRenderer.__validate_template(template_name)
        template = env.get_template(checked_name)
        return template.render(**context)
