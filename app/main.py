from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

# Import API logic
from src.api import router as api_router
from src.loader import load_documents_from_folder
from src.embedder import embed_text
from src.search import add_to_vector_store

app = FastAPI(title="PEERCORE-AILLM Knowledge Query API")

# Mount the static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Register the API router
app.include_router(api_router)

# Load and embed documents at startup
@app.on_event("startup")
def preload_docs():
    print("Loading documents")
    documents = load_documents_from_folder()

    for doc in documents:
        try:
            embedding = embed_text(doc["text"])
            add_to_vector_store(embedding, doc)
        except Exception as e:
            print(f"Failed to embed chunk: {doc['chunk_id']}\n{e}")
    
    print(f"Loaded {len(documents)} chunks into memory")

# Serve index.html at root
@app.get("/")
def root():
    return FileResponse(os.path.join("static", "index.html"))
