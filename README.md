# PEERCORE-AILLM: Document-Based Q&A API

Public Available link hosted on the cloud: http://54.160.213.114:8000

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
  git clone https://github.com/AmiruC/AI-LLM.git<br/>
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

## Environment Setup (.env)

This project requires AWS credentials and configuration values to be set in a `.env` file **which is not included in this repository** for security reasons.

Create a `.env` file in the root directory of the project with the following format:


AWS_ACCESS_KEY_ID=your-access-key-id
AWS_SECRET_ACCESS_KEY=your-secret-access-key
AWS_REGION=us-east-1
USE_AWS=true


## Design Decisions

Why Amazon Titan Embeddings?
This project uses Titan Embeddings via Amazon Bedrock to convert documents into dense vector representations. Titan was chosen for:
- High semantic relevance — Optimised for natural language understanding and similarity search
- Seamless AWS integration — Works with Boto3 and IAM
- Lightweight deployment — No need for local models or external databases

Why two models? Titan Embeddings & Titan Text G1?
- The app uses two different models because each serves a unique purpose. Amazon Titan Embeddings converts text into vector representations to semantically match user questions with relevant document chunks. Once the best chunk is found, Titan Text G1 generates a natural language answer based on that content, providing a clear and conversational response.

Why In-memory vectoring over FIASS?
- Simplicity and Portability - In-memory storage eliminates the need for complex setup, indexing, or persistence layers. It allows the entire application to remain lightweight and easily deployable with no external dependencies
- Tight Integration with Python - The in-memory solution works natively with Python data structures (e.g., NumPy arrays), reducing friction in development and debugging
- Perfect for lightweight proof of concept

## Sample Queries
You can ask simple questions like:
- "How do I reset my Apple ID password?"
- "How do I turn on low power mode?"
- "How do I set up face ID?"

You can ask complex questions like:
- "What colour is the iPhone SE, and does it have a home button?"
- "What storage and colour options does the iPhone 15 Pro come in?"





