from fastapi import APIRouter, Query
from src.embedder import embed_text
from src.search import search_similar_chunks
from src.generate_answer import generate_answer

# API for query
router = APIRouter()
@router.get("/query")
def query(q: str = Query(...)):
    try:
        # Step 1: Embed the user question
        query_embedding = embed_text(q)

        # Step 2: Retrieve top 3 similar chunks with threshold
        results = search_similar_chunks(query_embedding, top_k=3, threshold=0.5)

        if not results:
            return {
                "query": q,
                "natural_answer": "I'm sorry, I don't have information on that topic at the moment.",
                "results": []
            }

        # Step 3: Confidence check based on similarity score
        top_result = results[0]
        if top_result["score"] < 0.5:
            return {
                "query": q,
                "natural_answer": "I'm not confident enough to answer that question based on the available documents.",
                "results": results
            }

        # Step 4: Use top chunk as context for LLM answer
        top_context = top_result["text"]
        natural_answer = generate_answer(q, top_context)

        return {
            "query": q,
            "natural_answer": natural_answer,
            "results": results
        }

    except Exception as e:
        return {"error": str(e)}

