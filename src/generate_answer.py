import os
import json
import boto3
from dotenv import load_dotenv

# load env file for credentials 
load_dotenv()

# initialise bedrock client us-east-1 for guaranteed support 
client = boto3.client("bedrock-runtime", region_name=os.getenv("AWS_REGION", "us-east-1"))


# model use justified in README
MODEL_ID = "amazon.titan-text-lite-v1"  

# function to send GET request prompt change to ensure relevant answers only using given resource documents 
def generate_answer(question: str, context: str) -> str:
    prompt = (
      f"Based on the following information:\n{context}\n\n"
      f"Answer the question: {question}\n"
      "Please provide an answer using only the above information."
    )


    print("Sending prompt to Titan:", prompt)

    body = {
        "inputText": prompt
    }
    # get response as JSON object
    response = client.invoke_model(
        modelId=MODEL_ID,
        contentType="application/json",
        accept="application/json",
        body=json.dumps(body)  
    )

    output = json.loads(response["body"].read())
    print("Titan Response Raw:", output)
    # parse the JSON result for the output if no output return || No answer returned
    return output.get("results", [{}])[0].get("outputText", "[No answer returned]")

