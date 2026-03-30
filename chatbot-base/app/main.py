import os
import uuid
from dotenv import load_dotenv
from agents import Runner, SQLiteSession
from agent import chatbot_agent

def build_session():
    return SQLiteSession(f"chatbot_base_{uuid.uuid4().hex}")

def main():
    load_dotenv()

    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY is missing. Check your .env file.")
    
    # Create a session instance with a session ID
    session = build_session()


    print("Chatbot started. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye.")
            break

        if not user_input:
            continue

        result = Runner.run_sync(
            starting_agent=chatbot_agent,
            input=user_input,
            session=session,
        )
        answer = result.final_output

        print(f"\nAssistant: {answer}\n")

if __name__ == "__main__":
    main()