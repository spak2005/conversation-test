from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os

app = FastAPI()

@app.get("/")
async def root():
    return JSONResponse({"message": "OpenAI API integration is running"})

@app.post("/process")
async def process_text(message: str = "Hello"):
    try:
        # Just echo back a simple response for testing
        return JSONResponse({
            "response": f"Received: {message}",
            "api_key_exists": os.getenv("OPENAI_API_KEY") is not None
        })
    except Exception as e:
        return JSONResponse({"error": str(e)})

# This is needed for Vercel serverless deployment
handler = app 