# PEERCORE-AILLM: Document-Based Q&A API

PEERCORE-AILLM is a FastAPI-powered web service that enables intelligent querying over `.txt` and `.md` documents using Amazon Bedrock's Titan embeddings. It embeds documents into vector representations at startup, stores them **in memory**, and supports natural language queries with context-aware results and matched source chunks.

---

## 🧠 Features

- 📄 Load and parse documents (`.txt`, `.md`) from a folder  
- 🔍 Convert text into vector embeddings using **Amazon Bedrock (Titan Embeddings)**  
- ⚡ Perform in-memory similarity search (no database or FAISS needed)  
- 🤖 Answer questions with AI-generated responses + relevant source chunks  
- 🚀 FastAPI backend with Gunicorn deployment support  
- 📦 Lightweight and easy to deploy  

---

## 📁 Project Structure

AI-LLM/
│
├── app/
│ └── main.py # FastAPI entrypoint and startup logic
│
├── src/
│ ├── api.py # POST /query API route
│ ├── loader.py # Loads and chunks documents
│ ├── embedder.py # Bedrock embedding logic
│ ├── search.py # In-memory vector store & similarity match
│
├── static/ # Optional static frontend files
│ └── index.html
│
├── requirements.txt # Python dependencies
├── start.sh # Optional startup script
├── README.md # Project documentation

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/AI-LLM.git
cd AI-LLM
2. Create Virtual Environment
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
Make sure the following packages are included:
fastapi
uvicorn
gunicorn
boto3
sentence-transformers
python-dotenv
4. AWS Configuration (Bedrock Access)
Ensure AWS credentials are available via ~/.aws/credentials or environment variables. You must have access to Bedrock and permissions to call InvokeModel.
🚀 Run the API

Development (hot reload):
uvicorn app.main:app --reload
Production (Gunicorn):
gunicorn app.main:app --workers 1 --bind 0.0.0.0:8000
📬 API Usage

POST /query
Ask a natural language question.
Request:
{
  "question": "What is the purpose of this system?"
}
Response:
{
  "answer": "This system allows querying documents using Bedrock embeddings...",
  "matches": [
    {
      "chunk_id": "doc-01-chunk-03",
      "text": "This API enables intelligent Q&A over uploaded documents."
    }
  ]
}
🧠 Design Decisions

In-memory vector storage was used to simplify deployment and optimize speed for smaller-scale use cases.
Amazon Bedrock Titan Embeddings were chosen for secure, scalable, high-quality embeddings without self-hosting models.
Avoided external databases or vector DBs to reduce infrastructure complexity.
🌐 Sample Questions

"What does the preload function do?"
"Which documents are loaded on startup?"
"How is the vector search implemented?"
🏗️ Architecture Overview

[Markdown/.txt Files] --> [Chunking] --> [Titan Embeddings via Bedrock]
           |
        [In-Memory Vector Store] <--> [Similarity Search]
           |
        [FastAPI] <--> [User Query Input]
