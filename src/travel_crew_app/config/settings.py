from __future__ import annotations

from dataclasses import dataclass

from crewai import LLM


@dataclass
class Settings:
    # Name of the model as seen by Ollama
    # e.g. `ollama run llama3` → model id is "llama3"
    ollama_model: str = "ollama/gemma3"
    base_url: str = "http://localhost:11434"
    temperature: float = 0.3


settings = Settings()


def get_llm() -> LLM:
    """
    Return a CrewAI LLM pointing to your local Ollama server.
    No OpenAI key needed.
    """
    return LLM(
        model=settings.ollama_model,
        base_url=settings.base_url,
        temperature=settings.temperature,
    )
