from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "Tauji aur Sensitivity Dono Server Ekdum Live Hain!"}

# 1. PEHLA APP: Free Fire Sensitivity App ka rasta
@app.post("/sensitivity-chat")
def get_sensitivity_response(request: ChatRequest):
    user_msg = request.message.lower()
    if "sensivity" in user_msg or "sensitivity" in user_msg or "ff" in user_msg:
        return {
            "response": "Re chore! iQOO z10x ki lath gaad Sensitivity ye le:\n\n🎯 General: 98\n🔴 Red Dot: 95\n🔍 2X Scope: 90\n🔭 4X Scope: 88\n\nIse laga le, fir dekh saare headshot lagenge! 😉"
        }
    return {"response": "Ram Ram bhai! Free Fire ki sensitivity jaan-ni hai toh device ka naam sahi se likho!"}

# 2. DUSRA APP: Asli Desi AI Chatbot (Tauji) ka rasta
@app.post("/desi-tauji-chat")
def get_tauji_response(request: ChatRequest):
    user_msg = request.message.lower()
    
    if "kaise ho" in user_msg or "ram ram" in user_msg:
        return {"response": "Ram Ram re chore! Ib tera Tau ekdum raaji-khushi se. Tu bata ke khichdi pakh rhi se tere dimaag me?"}
    
    elif "shayari" in user_msg or "joke" in user_msg:
        return {"response": "Kade dhoop me ghumme, kade chaav me ghumme...\nArre asli maza toh chore jab Tau haryanvi me jhaad dikhaave! 😂"}
    
    else:
        return {"response": "Re chore, ib dhang ki baat pooch le Tau te, yo tera naya server ekdum lath gaad chal rya se! 🌾"}
