from enum import StrEnum, auto

class WhisperMode(StrEnum):
    """An enum of the possible Whisper modes."""
    TRANSCRIBE = auto()
    TRANSLATE = auto()