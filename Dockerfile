FROM ubuntu:22.04

# Zaroori packages install karna (zstd bhi jodh diya hai)
RUN apt-get update && apt-get install -y curl python3 python3-pip zstd

# Ollama install karna
RUN curl -fsSL https://ollama.com/install.sh | sh

# Python libraries install karna
RUN pip3 install fastapi uvicorn pydantic requests

WORKDIR /code

COPY . .

# Ek script jo Ollama aur FastAPI dono ko chalu karegi
CMD ["sh", "start.sh"]