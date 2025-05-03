# this handles the in-memory vector search 

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# In-memory storage of vectors ie database to replace the use of FAISS
vector_store = []  

def add_to_vector_store(embedding: list[float], metadata: dict):
    # append to vector_store as this object format || Get vector + Metadata of vector 
    vector_store.append({
        "embedding": np.array(embedding),
        "text": metadata["text"],
        "source": metadata["source"],
        "chunk_id": metadata["chunk_id"]
    })

def search_similar_chunks(query_embedding: list[float], top_k: int = 3, threshold: float = 0.5) -> list[dict]: #define query_embedding as a list of floats
    # need to transform the vector array into a matrix 2D array for the input of cosine similarity
    query_vec = np.array(query_embedding).reshape(1, -1)

    #  catch for empty vector array 
    if not vector_store:
        return []


    all_embeddings = np.array([item["embedding"] for item in vector_store])
    similarities = cosine_similarity(query_vec, all_embeddings)[0]

    # Filter out results for only above the threshold
    filtered_indices = [i for i, score in enumerate(similarities) if score >= threshold]

    if not filtered_indices:
        return []

    # Sort the filtered results by similarity score in descending order
    sorted_indices = sorted(filtered_indices, key=lambda i: similarities[i], reverse=True)[:top_k]

    results = []
    for idx in sorted_indices:
        item = vector_store[idx]
        results.append({
            "text": item["text"],
            "source": item["source"],
            "chunk_id": item["chunk_id"],
            "score": float(similarities[idx])
        })

    return results
