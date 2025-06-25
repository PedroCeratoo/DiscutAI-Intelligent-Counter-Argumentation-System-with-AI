# 🧠 DiscutAI — Sistema Inteligente de Contra-Argumentação com IA

DiscutAI é um sistema interativo que utiliza **modelos de linguagem natural (LLMs)** para gerar contra-argumentações educativas de maneira clara, respeitosa e acessível, especialmente voltadas para alunos do ensino fundamental.

---

## 🖥️ Interface

A interface foi desenvolvida com **HTML, CSS e JavaScript**, com foco na simplicidade e na usabilidade.

A comunicação entre o frontend e o backend é feita através de uma requisição HTTP (`fetch`) para a API. O código da interface está disponível neste repositório, ou pode ser acessado diretamente no seguinte link:

🔗 **[DiscutAI - Intelligent Counter-Argumentation System with AI](https://github.com/)**  
*(insira o link correto do seu repositório)*

---

## 🧰 Bibliotecas Utilizadas

### Principais

- **FastAPI**  
  Framework moderno e assíncrono para criação de APIs RESTful com Python.

- **Pydantic**  
  Utilizada para validação e tipagem de dados, garantindo a integridade das mensagens trocadas via API.

### Utilitárias

- **CORSMiddleware**  
  Middleware que habilita o compartilhamento de recursos entre diferentes origens (CORS), permitindo o consumo da API por interfaces externas.

- **Requests**  
  Biblioteca usada para enviar requisições HTTP ao modelo de linguagem rodando localmente via **Ollama**.

- **Typing (`Dict`, `List`, `Optional`)**  
  Fornece suporte à anotação de tipos no código, tornando-o mais seguro e compreensível.

---

## ⚙️ Funcionamento

1. O usuário acessa a interface e envia uma **mensagem textual**.
2. A mensagem é enviada para a API backend.
3. A API estrutura o prompt e o envia para um modelo de linguagem (como `gemma` ou `llama3`) executado localmente via **Ollama**.
4. O modelo retorna uma **contra-argumentação** que é devolvida ao usuário de forma simples, empática e didática.

---

## 🔍 Descrição do Código

### 📦 Importações

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests
from typing import Dict, Optional, List
