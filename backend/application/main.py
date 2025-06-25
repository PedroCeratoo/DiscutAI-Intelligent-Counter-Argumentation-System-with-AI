from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests
from typing import Dict
from typing import Optional, List, Dict

class MensagemEntrada(BaseModel):
    mensagem: str
    historico: Optional[List[Dict[str, str]]] = None

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
    resposta = gerar_resposta_ollama(
        user_input=mensagem.mensagem,
        historico=mensagem.historico
    )
    return {"resposta": resposta}



def gerar_resposta_ollama(user_input: str, historico: list = None) -> str:
    url = "http://localhost:11434/api/generate"

    historico_texto = ""
    if historico:
        for mensagem in historico:
            if "aluno" in mensagem:
                historico_texto += f"Aluno: {mensagem['aluno']}\n"
            if "discutai" in mensagem:
                historico_texto += f"DiscutAI: {mensagem['discutai']}\n"

    prompt_base = (
        "Você é o DiscutAI, um assistente educacional que ajuda alunos do ensino fundamental a pensar criticamente.\n"
        "Responda apenas a mensagens que contenham opiniões, argumentos ou teses, com uma contra-argumentação simples, respeitosa e fácil de entender.\n"
        "Use linguagem acessível para crianças, exemplos concretos e evite termos técnicos.\n\n"
        f"{historico_texto}"
        f"Aluno: {user_input}\n"
        "DiscutAI:"
    )

    payload = {
        "model": "gemma",
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

