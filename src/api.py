from fastapi import APIRouter, Query
from src.embedder import embed_text
from src.search import search_similar_chunks
from src.generate_answer import generate_answer

# API for query
router = APIRouter()

@router.get("/query")
def query(q: str = Query(...)):
    try:
        # Embed the users question
        query_embedding = embed_text(q)
        # Find the most similar document chunks top 3
        results = search_similar_chunks(query_embedding, top_k=3, threshold=0.5)  # <— pass threshold

        # If results are empty due to not meeting criteria 
        if not results:
            return {
                "query": q,
                "natural_answer": "I'm sorry, I don't have information on that topic at the moment.",
                "results": []
            }
        # This only takes the top most relevant source to stop confusion on the Titan model
        top_context = results[0]["text"]

        # Send the question to Titan Text G1 model on bedrock
        natural_answer = generate_answer(q, top_context)

        return {
            "query": q,
            "natural_answer": natural_answer,
            "results": results
        }

    except Exception as e:
        return {"error": str(e)}
