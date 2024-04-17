from pydantic import BaseModel

class RateLimits(BaseModel):
    """Represents the rate limits by models for free users."""
    LLM: str
    STABLEDIFFUSION: str
    STABLEDIFFUSIONXL: str
    IMG2IMG: str
    TEXT2GIF: str
    WHISPER: str
    IMAGEUPSCALING: str
    MIDJOURNEY: str

class Tiers(BaseModel):
    """Represents tiers from VisionCraft API."""
    FREE: RateLimits
    TIER_1: RateLimits
    TIER_2: RateLimits