# PEERCORE-AILLM: Document-Based Q&A API

PEERCORE-AILLM is a FastAPI-powered service that enables intelligent, context-aware querying of .txt and .md documents using Amazon Bedrock’s Titan Embeddings.<br/>

At startup, the system loads documents, splits them into chunks, embeds each into high-dimensional vectors, and stores them in memory for fast retrieval. Users can then ask natural language questions and receive semantically relevant answers, including:<br/>

A natural language response generated from the best-matched content<br/>
The original source chunk(s) used<br/>
A relevance score indicating match confidence<br/>
A lightweight frontend interface is also included to interactively explore the document knowledge base.<br/>

🚀 Features:

1. 📄 Load and parse .txt and .md documents from a local folder
2. 🔍 Generate vector embeddings using Amazon Bedrock (Titan)
3. 🧠 In-memory similarity search (no database or FAISS required)
4. 🤖 Natural language AI-generated answers with supporting source chunks
5. 🧪 FastAPI backend with Gunicorn deployment support
6. ⚙️ Lightweight, portable, and easy to deploy



## Setup Instructions

1. Clone the Repository <br/>
  git clone https://github.com/yourusername/AI-LLM.git<br/>
  cd AI-LLM

3. Create Virtual Environment<br/>
python3 -m venv venv<br/>
source venv/bin/activate

5. Install Dependencies<br/>
pip install -r requirements.txt<br/>
Make sure the following packages are listed in requirements.txt:<br/>
fastapi<br/>
uvicorn<br/>
gunicorn<br/>
boto3<br/>
sentence-transformers<br/>
python-dotenv<br/>

7. Run in Development Mode<br/>
uvicorn app.main:app --reload<br/>

## Design Decisions

Why Amazon Titan Embeddings?
This project uses Titan Embeddings via Amazon Bedrock to convert documents into dense vector representations. Titan was chosen for:
- High semantic relevance — Optimised for natural language understanding and similarity search
- Seamless AWS integration — Works with Boto3 and IAM
- Lightweight deployment — No need for local models or external databases

Why In-memory vectoring over FIASS?
- Simplicity and Portability - In-memory storage eliminates the need for complex setup, indexing, or persistence layers. It allows the entire application to remain lightweight and easily deployable with no external dependencies
- Tight Integration with Python - The in-memory solution works natively with Python data structures (e.g., NumPy arrays), reducing friction in development and debugging
- Perfect for lightweight proof of concept

## Sample Queries
You can ask simple questions like:
- "How do I reset my Apple ID password?"
- "What are the current iPhone models?"
- "How do I turn on low power mode?"

You can ask complex questions like:
- "What colour is the iPhone SE, and does it have a home button?"
- "What storage and colour options does the iPhone 15 Pro come in?"





