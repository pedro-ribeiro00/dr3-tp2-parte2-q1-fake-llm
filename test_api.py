from fastapi.testclient import TestClient
from main import app

def test_chat():
    client = TestClient(app)
    result = client.post("/chat", json={"text":"Qual é o seu nome?"})
    assert result.status_code == 200
    assert "Fake LLM" in result.json()["answer"]
    assert result.json()["simulated"] is True
    assert "pré-definida" in client.post("/chat", json={"text":"xyz"}).json()["answer"]
    assert client.post("/chat", json={"text":" "}).status_code == 422
