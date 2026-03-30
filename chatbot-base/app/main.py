import os
from dotenv import load_dotenv
from agents import Runner
from agent import chatbot_agent

def main():
    load_dotenv()

    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY is missing. Check your .env file.")

    history = []

    print("Chatbot started. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye.")
            break

        if not user_input:
            continue

        history.append({"role": "user", "content": user_input})

        result = Runner.run_sync(chatbot_agent, history)
        answer = result.final_output

        print(f"\nAssistant: {answer}\n")

        history.append({"role": "assistant", "content": answer})

if __name__ == "__main__":
    main()