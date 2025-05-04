# PEERCORE-AILLM: Document-Based Q&A API

PEERCORE-AILLM is a FastAPI-powered service that enables intelligent, context-aware querying of .txt and .md documents using Amazon Bedrock’s Titan Embeddings.
At startup, the system loads documents, splits them into chunks, embeds each into high-dimensional vectors, and stores them in memory for fast retrieval. Users can then ask natural language questions and receive semantically relevant answers, including:
A natural language response generated from the best-matched content
The original source chunk(s) used
A relevance score indicating match confidence
A lightweight frontend interface is also included to interactively explore the document knowledge base.

🚀 Features:

📄 Load and parse .txt and .md documents from a local folder
🔍 Generate vector embeddings using Amazon Bedrock (Titan)
🧠 In-memory similarity search (no database or FAISS required)
🤖 Natural language AI-generated answers with supporting source chunks
🧪 FastAPI backend with Gunicorn deployment support
⚙️ Lightweight, portable, and easy to deploy
📁 Project Structure

AI-LLM/
├── app/
│   └── main.py           # FastAPI entry point
│
├── src/
│   ├── api.py            # API endpoint for question answering
│   ├── loader.py         # Loads and chunks documents
│   ├── embedder.py       # Embeds text using Titan
│   ├── search.py         # In-memory search & similarity scoring
│
├── static/               # Optional frontend
│   └── index.html
│
├── requirements.txt      # Python dependencies
├── start.sh              # Optional startup script
├── README.md             # Project documentation


⚙️ Setup Instructions

1. Clone the Repository
git clone https://github.com/yourusername/AI-LLM.git
cd AI-LLM

3. Create Virtual Environment
python3 -m venv venv
source venv/bin/activate

5. Install Dependencies
pip install -r requirements.txt
Make sure the following packages are listed in requirements.txt:
fastapi
uvicorn
gunicorn
boto3
sentence-transformers
python-dotenv

7. Run in Development Mode
uvicorn app.main:app --reload

🧠 Design Decisions

Why Amazon Titan Embeddings?
This project uses Titan Embeddings via Amazon Bedrock to convert documents into dense vector representations. Titan was chosen for:
- High semantic relevance — Optimised for natural language understanding and similarity search
- Seamless AWS integration — Works with Boto3 and IAM
- Lightweight deployment — No need for local models or external databases

Why In-memory vectoring over FIASS?
- Simplicity and Portability - In-memory storage eliminates the need for complex setup, indexing, or persistence layers. It allows the entire application to remain lightweight and easily deployable with no external dependencies
- Tight Integration with Python - The in-memory solution works natively with Python data structures (e.g., NumPy arrays), reducing friction in development and debugging
- Perfect for lightweight proof of concept






