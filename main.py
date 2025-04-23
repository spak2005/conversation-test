from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables - works locally
load_dotenv()

# Create FastAPI app
app = FastAPI()

# Define our request model
class InputText(BaseModel):
    message: str

# Initialize OpenAI client - use environment variable from Vercel in production
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

@app.get("/")
async def root():
    return {"message": "OpenAI API integration is running"}

@app.post("/process")
async def process_text(data: InputText):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": data.message}]
        )
        return {"response": response.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)}

# For local development
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)