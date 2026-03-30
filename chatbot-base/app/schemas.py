from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, description="User message")
    session_id: str = Field(..., min_length=1, description="Conversation session ID")


class ChatResponse(BaseModel):
    answer: str
    session_id: str