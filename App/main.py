from fastapi import FastAPI
import requests

app = FastAPI()

@app.post("/chat")
async def chat(user_input: str):
    # This calls your local Ollama instance
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral", "prompt": user_input, "stream": False}
    )
    return response.json()