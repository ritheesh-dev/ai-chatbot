README.md Template
Local AI Chat Application
This project is a full-stack, locally hosted AI chatbot. It uses a FastAPI backend to manage requests and a Streamlit frontend for a clean user interface. The AI logic is powered by Ollama, allowing you to run Large Language Models (LLMs) like Mistral entirely on your own machine.

🏗️ Architecture

Frontend: Streamlit (Python-based UI)

Backend: FastAPI (REST API)

Model Provider: Ollama (Local LLM Runtime)

Model: Mistral

🚀 Getting Started

1. Prerequisites
Python 3.9+

Ollama installed and running.

The Mistral model pulled locally:

ollama pull mistral

2. Installation

pip install -r requirements.txt

3. Running the Application
You need to run two separate terminals for this application:

Terminal 1: Start the Backend (FastAPI)

uvicorn main:app --reload
The backend will run at http://localhost:8000.

Terminal 2: Start the Frontend (Streamlit)

streamlit run frontend.py
The frontend will open in your browser at http://localhost:8501.

📂 Project Structure
frontend.py: The Streamlit interface code.

main.py: The FastAPI backend handling model logic.

requirements.txt: List of necessary Python libraries.

.gitignore: Prevents unnecessary files from being uploaded to GitHub.

🛠️ How it Works
The user enters a prompt in the Streamlit UI.

Streamlit sends a POST request to the FastAPI /chat endpoint.

FastAPI forwards the prompt to the local Ollama API (port 11434).

The model generates a response, which travels back through the API to be displayed on your screen.