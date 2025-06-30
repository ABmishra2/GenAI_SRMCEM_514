from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os

# Replace with your actual key or use environment variable
openai.api_key = os.getenv("OPENAI_API_KEY", "your-openai-api-key-here")

app = FastAPI()

# Define the request model
class PromptRequest(BaseModel):
    prompt: str
    max_tokens: int = 100

# Basic route to test the API
@app.get("/")
def read_root():
    return {"message": "Welcome to the OpenAI FastAPI Text Generator"}

# AI text generation endpoint
@app.post("/generate/")
def generate_text(data: PromptRequest):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # or "gpt-3.5-turbo-instruct"
            prompt=data.prompt,
            max_tokens=data.max_tokens,
            temperature=0.7
        )
        return {"response": response.choices[0].text.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
