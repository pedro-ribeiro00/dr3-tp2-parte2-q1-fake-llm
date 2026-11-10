from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator
from langchain_core.language_models.fake import FakeListLLM

app = FastAPI()
respostas = {
    "olá": "Olá! Como posso ajudar?",
    "qual é o seu nome": "Sou um chatbot de teste.",
    "o que é fastapi": "FastAPI é um framework Python para criar APIs.",
}


class Entrada(BaseModel):
    text: str = Field(min_length=1, max_length=20000)

    @field_validator("text")
    @classmethod
    def validar_texto(cls, texto):
        if not texto.strip():
            raise ValueError("Informe um texto.")
        return texto

@app.post("/chat")
def conversar(entrada: Entrada):
    pergunta = entrada.text.lower().strip().rstrip("?.!")
    resposta = respostas.get(pergunta, "Não tenho uma resposta para essa pergunta.")
    modelo = FakeListLLM(responses=[resposta])
    return {"answer": modelo.invoke(entrada.text)}
