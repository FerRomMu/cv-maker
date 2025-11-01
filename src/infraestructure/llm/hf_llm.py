import os
from abc import override

from huggingface_hub import InferenceClient

from src.domain.services.llm import LlmService


class HfLLM(LlmService):

    def __init__(self, model: str = "deepseek-ai/DeepSeek-V3-0324"):
        token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
        if not token:
            raise ValueError("Falta HUGGINGFACEHUB_API_TOKEN en el entorno.")
        self.client = InferenceClient(model=model, token=token)

    @override
    def query(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            max_tokens=128,
        )
        return response.choices[0].message["content"]
