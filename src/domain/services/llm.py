from abc import ABC, abstractmethod
from typing import Any


class LlmService(ABC):
    @abstractmethod
    def query(self, prompt: str, **kwargs: Any) -> str:
        """Envía un prompt al LLM y devuelve la respuesta en texto."""
        pass
