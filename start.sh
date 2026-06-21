#!/bin/bash

# Background me Ollama chalu karna
ollama serve &

# Ollama ke chalu hone ka thoda wait karna
sleep 5

# Server start hote hi 'phi3' model ko background me load karke ready rakhna
ollama run phi3 "ram ram"

# Apna FastAPI server start karna
uvicorn main:app --host 0.0.0.0 --port 7860