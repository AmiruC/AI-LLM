from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# import api logic 
from src.api import router as api_router
from src.loader import load_documents_from_folder
from src.embedder import embed_text
from src.search import add_to_vector_store


app = FastAPI(title="PEERCORE-AILLM Knowledge Query API")

# Define the index file to display 
app.mount("/static", StaticFiles(directory="static"), name="static")

#Call api logic
app.include_router(api_router)

# Load and embed documents at startup
@app.on_event("startup")
def preload_docs():
    print("Loading documents")
    documents = load_documents_from_folder()

    for doc in documents:
        # TRY..EXCEPTION to catch error with file embedding 
        try:
            embedding = embed_text(doc["text"])
            # send the documents for embedding
            add_to_vector_store(embedding, doc)
        except Exception as e:
            print(f"Failed to embed chunk: {doc['chunk_id']}\n{e}")
    
    print(f"Loaded {len(documents)} chunks into memory")

@app.get("/")
def root():
    return {"message": "PEERCORE-AILLM"}
