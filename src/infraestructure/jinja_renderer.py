from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from src.infraestructure.config.paths import TEMPLATES
from src.infraestructure.latex_filter import latex_escape


class JinjaRenderer:

    def __init__(self, template_dir: Path = TEMPLATES):
        self.template_dir = template_dir
        self.env = Environment(
            loader=FileSystemLoader(template_dir), autoescape=False
        )
        self.__register_filters()

    def __register_filters(self):
        self.env.filters["latex_escape"] = latex_escape

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

    def render(
        self,
        template_name: str,
        context: dict,
    ) -> str:
        checked_name = self.__validate_template(template_name)
        template = self.env.get_template(checked_name)
        return template.render(**context)
