import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()  # Carrega as variáveis do .env

api_key = os.getenv("GENAI_API_KEY")

if not api_key:
    raise Exception("A variável GENAI_API_KEY não está definida no .env")

genai.configure(api_key=api_key)

model = genai.GenerativeModel('models/gemini-1.5-flash-latest')

prompt_base = """..."""

def perguntar_ao_bot(pergunta):
    prompt = f"{prompt_base}\nUsuário: {pergunta}\nLimpinha:"
    resposta = model.generate_content(prompt)
    return resposta.text.strip()
