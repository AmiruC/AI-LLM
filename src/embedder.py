# file to embed the documents into vectors

import os
import json
import boto3
from dotenv import load_dotenv

load_dotenv()

# Get environment values for aws credentials 
# It is set to false from default for testing. However for this project it is assigned "True" to uilise AWS Bedrock models
USE_AWS = os.getenv("USE_AWS", "false").lower() == "true"

# if not using AWS for testing 
if not USE_AWS:
    # run locally transformer
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("all-MiniLM-L6-v2")

    def embed_text(text: str) -> list[float]:
        return model.encode(text).tolist()

# for the project enabled AWS Bedrock(titan)
else:
    # creating boto3 client for AWS Bedrock titan embedding model 
    client = boto3.client("bedrock-runtime", region_name=os.getenv("AWS_REGION", "us-east-1"))
    MODEL_ID = "amazon.titan-embed-text-v1"

    # sending payload to AWS
    def embed_text(text: str) -> list[float]:
        payload = {"inputText": text}
        response = client.invoke_model(
            modelId=MODEL_ID,
            contentType="application/json",
            accept="application/json",
            body=json.dumps(payload)
        )
        body = json.loads(response["body"].read())
        return body["embedding"]
