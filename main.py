import unicodedata
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_core.language_models.fake import FakeListLLM
from langchain_core.prompts import PromptTemplate
from schemas import TextRequest

app = FastAPI(title="Parte 2 - Q1 - Fake LLM")
ANSWERS = {
    "ola": "Olá! Como posso ajudar?",
    "qual e o seu nome": "Sou um chatbot de demonstração com Fake LLM.",
    "o que e fastapi": "FastAPI é um framework Python para criar APIs.",
}
prompt = PromptTemplate.from_template("Pergunta: {question}\nResposta:")

class ChatResponse(BaseModel):
    answer: str
    simulated: bool = True

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse)
def chat(data: TextRequest):
    normalized = unicodedata.normalize("NFKD", data.text.lower())
    normalized = "".join(c for c in normalized if not unicodedata.combining(c))
    key = normalized.strip().rstrip("?!.")
    response = ANSWERS.get(key, "Não tenho uma resposta pré-definida para essa pergunta.")
    # Instância por pedido: nenhuma posição compartilhada entre requisições.
    fake = FakeListLLM(responses=[response])
    chain = prompt | fake
    return {"answer": chain.invoke({"question": data.text}), "simulated": True}
