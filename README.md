# llm_playground
Playground to learn about AI agents

## Steps

To start terminal session (linux):

```source .venv/bin/activate```  

For windows:  

`.venv\Scripts\Activate.ps1`

May need to use this before:

`Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`

For installing agents SDK:

`pip install openai-agents`


## First-agent Folder

Following quickstar from OpenAI Agents SDK: <https://openai.github.io/openai-agents-python/quickstart/>

## Chatbot-base Folder

Simple chatbot implementation with:
- Python backend
- HTTP route with FastAPI
- single conversational agent
- in-memory message history
- clear instructions
- project structure designed to scale