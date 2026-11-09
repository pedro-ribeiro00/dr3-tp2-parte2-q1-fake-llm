# Chatbot com Fake LLM

DR3 - TP2. Python 3.11 ou 3.12. Execute os comandos dentro desta pasta.

## Instalação

```bash
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Execução

```bash
uvicorn main:app --host 127.0.0.1 --port 8000
```

Abra http://127.0.0.1:8000/docs para testar pelo Swagger. Pare uma aplicação antes de iniciar outra na mesma porta. O endpoint `/health` confirma que o startup terminou.

```bash
curl -X POST http://127.0.0.1:8000/chat -H "Content-Type: application/json" -d '{"text":"qual é o seu nome?"}'
```

No PowerShell, use o Swagger ou `curl.exe`. Entrada inválida retorna 422. Falhas de serviço são documentadas no código. Não há autenticação pública: executar como protótipo local.

## Testes

```bash
python -m pytest -q
```

Os testes de contrato substituem a inferência para validar HTTP sem download nem cobrança. Eles não medem qualidade do modelo. Consulte `VALIDACAO.md` na raiz da entrega para as verificações realmente executadas.

Para repetir as versões diretas usadas na validação, instale `requirements-testadas.txt` no lugar de `requirements.txt`. Os pacotes transitivos ainda são resolvidos pelo pip.

## Formato de saída

Exemplo ilustrativo; gerações reais podem variar.

```json
{
  "answer": "Sou um chatbot de demonstração com Fake LLM.",
  "simulated": true
}
```
