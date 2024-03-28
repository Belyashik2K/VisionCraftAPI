from pydantic import BaseModel

class LLMAnswer(BaseModel):
    """Represents the answer from the LLM model."""
    role: str
    content: str