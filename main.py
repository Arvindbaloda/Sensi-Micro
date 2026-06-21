from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MY_SECRET_KEY = "meri-desi-ai-key-123"

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "Desi AI Server is Online!"}

@app.post("/v1/chat")
async def chat_with_local_ai(request: ChatRequest, authorization: str = Header(None)):
    if not authorization or authorization != f"Bearer {MY_SECRET_KEY}":
        raise HTTPException(status_code=401, detail="Arre bhai, galat API key h!")
    
    ollama_url = "http://127.0.0.1:11434/api/generate"
    payload = {
        "model": "phi3",  # Ekdum correct aur tested model name
        "prompt": request.message,
        "stream": False   # Normal fast JSON response ke liye
    }
    
    try:
        response = requests.post(ollama_url, json=payload)
        response_data = response.json()
        
        # Agar Ollama sahi response de toh bhejो, nahi toh error pakdo
        if "response" in response_data:
            return {"reply": response_data["response"]}
        else:
            return {"reply": "Ollama chal toh raha hai par reply khali hai!"}
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")