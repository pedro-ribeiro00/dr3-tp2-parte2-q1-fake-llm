# Parte 2 - Questão 1: Fake LLM

## Como executar

Use Python 3.11 ou 3.12. Dentro desta pasta, crie um ambiente e instale as dependências:

```bash
python -m venv .venv
```

Ative o ambiente:

```bash
# Linux ou macOS
source .venv/bin/activate
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

```bash
python -m pip install -r requirements.txt
uvicorn main:app --port 8000
```

Abra http://127.0.0.1:8000/docs, selecione POST /chat, clique em “Try it out” e envie:

```json
{"text": "qual é o seu nome?"}
```

Também é possível enviar pelo terminal (no Windows, use curl.exe):

```bash
curl -X POST http://127.0.0.1:8000/chat -H "Content-Type: application/json" -d '{"text":"qual é o seu nome?"}'
```

Execute uma aplicação por vez na porta 8000. Textos vazios são recusados com erro 422.

Perguntas disponíveis: “olá”, “qual é o seu nome?” e “o que é fastapi?”. Outras entradas recebem uma resposta padrão. O FakeListLLM simula a resposta; não há chamada a um modelo real. A resposta tem o campo `answer`.
