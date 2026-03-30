import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from agents import Runner, SQLiteSession

from app.agent import chatbot_agent
from app.schemas import ChatRequest, ChatResponse

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY is missing. Check your .env file.")

app = FastAPI(title="Chatbot Base API")

# Simple in-memory cache of session objects by session_id
sessions: dict[str, SQLiteSession] = {}


def get_or_create_session(session_id: str) -> SQLiteSession:
    if session_id not in sessions:
        sessions[session_id] = SQLiteSession(session_id)
    return sessions[session_id]


@app.get("/")
async def root():
    return {"status": "ok", "message": "Chatbot API is running"}


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        session = get_or_create_session(request.session_id)

        result = await Runner.run(
            starting_agent=chatbot_agent,
            input=request.message,
            session=session,
        )

        return ChatResponse(
            answer=result.final_output,
            session_id=request.session_id,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))