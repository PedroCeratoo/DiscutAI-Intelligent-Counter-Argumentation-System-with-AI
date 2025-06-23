from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests
from typing import Dict

class MensagemEntrada(BaseModel):
    mensagem: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/debate")
def debater(mensagem: MensagemEntrada):
    resposta = gerar_resposta_ollama(mensagem.mensagem)
    return {"resposta": resposta}


def gerar_resposta_ollama(user_input: str) -> str:
    url = "http://localhost:11434/api/generate"
    
    # Prompt base (contexto do sistema)
    prompt_base = (
        "Você é um bot de contra argumentação chamado DiscutAI. "
        "Seu papel é ajudar alunos do ensino fundamental a pensar criticamente. "
        "Dada uma afirmação ou opinião, sua tarefa é apresentar uma contra-argumentação clara, "
        "respeitosa, sucinta e com linguagem apropriada para crianças. "
        "Evite termos complexos e use exemplos simples quando possível.\n\n"
        "Quando possível, cite dados ou artigos científicos para dar credibilidade na sua resposta\n\n"
        f"Afirmativa do aluno: {user_input}\n"
        "Contra-argumento:"
    )
    
    payload = {
        "model": "gemma",  # ou "llama3" se estiver usando outro modelo
        "prompt": prompt_base,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload, timeout=60)
        response.raise_for_status()
        resultado = response.json()
        return resultado.get("response", "Erro: sem resposta do modelo.")
    except Exception as e:
        return f"Erro ao gerar resposta: {e}"
