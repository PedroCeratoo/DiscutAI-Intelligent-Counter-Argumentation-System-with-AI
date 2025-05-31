from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from fastapi.middleware.cors import CORSMiddleware

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

chatbot = pipeline("text-generation", model="gpt2", max_new_tokens=200)

@app.post("/api/debate")
async def gerar_resposta(mensagem: MensagemEntrada):
    prompt = (
        f"Você é DiscutAI, um debatedor inteligente e rigoroso. "
        f"Sua única função é sempre contra-argumentar de forma lógica, educada e bem fundamentada, mesmo que o argumento do usuário pareça correto. "
        f"Não concorde, não elogie, apenas refute ou apresente um ponto de vista alternativo. "
        f"Sua resposta deve ser exclusivamente em português do Brasil.\n\n"
        f"Argumento do Usuário: {mensagem.mensagem}\nDiscutAI:"
    )
    resultado = chatbot(prompt, do_sample=True, temperature=0.7)[0]["generated_text"]
    resposta = resultado.split("DiscutAI:")[-1].strip()
    return {"resposta": resposta}


