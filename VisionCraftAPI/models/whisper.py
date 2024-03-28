from typing import List, Optional
from pydantic import BaseModel

class InferenceStatus(BaseModel):
    """Represents the status of the inference."""
    status: str
    runtime_ms: int
    cost: float
    tokens_generated: Optional[int]
    tokens_input: Optional[int]

class Segment(BaseModel):
    """Represents a segment from the Whisper model."""
    id: int
    seek: int
    start: float
    end: float
    text: str
    tokens: List[int]
    temperature: float
    avg_logprob: float
    compression_ratio: float
    no_speech_prob: float

class WhisperResult(BaseModel):
    """
    Represents the result from the Whisper model.
    """
    request_id: str
    inference_status: InferenceStatus
    text: str
    segments: List[Segment]
    language: str
    input_length_ms: int
