from agents import Agent

chatbot_agent = Agent(
    name="ChatbotBase",
    instructions=(
        "You are a helpful, clear, and concise assistant. "
        "Answer in English unless the user asks for another language. "
        "If you do not know something, say so clearly. "
        "Do not invent facts."
    ),
)