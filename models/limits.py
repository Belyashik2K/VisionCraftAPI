from pydantic import BaseModel

class RateLimits(BaseModel):
    """Represents the rate limits by models for free users."""
    LLM: str
    STABLEDIFFUSION: str
    STABLEDIFFUSIONXL: str
    DALLE3: str
    OPENJOURNEY: str
    IMG2IMG: str
    TEXT2GIF: str
    WHISPER: str
    IMAGEUPSCALING: str
    MIDJOURNEY: str
