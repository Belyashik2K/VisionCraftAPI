from typing import Optional
from pydantic import BaseModel

class MidjourneyTask(BaseModel):
    """Represents the task for the Midjourney model."""
    statusCode: int
    message: str
    data: int
    
class MidjourneyResult(BaseModel):
    """Represents the result from the Midjourney model."""
    ImageID: int
    Status: str
    StartTime: Optional[str] = None
    RequestTime: Optional[str] = None
    FinishTime: Optional[str] = None
    URL: Optional[str] = None