# 🧼 Limpinha – Sua Assistente Virtual de Tarefas Domésticas

**Limpinha** é um chatbot inteligente e simpático, criado para auxiliar **donas de casa e diaristas** com dicas práticas de limpeza, organização da casa e pequenas tarefas do dia a dia.  

Ela fala como uma amiga de confiança, sabe como tirar gordura do fogão, mancha de mofo da parede ou até montar um cronograma de faxina da semana.

> 💬 Desenvolvido como parte de uma **competição de chatbots**, com foco em utilidade prática, linguagem acessível e empatia no atendimento.

---

## ✨ Funcionalidades

- 🧠 **Respostas contextualizadas** com linguagem simples e carismática
- 🧼 **Dicas de limpeza doméstica** (produtos, misturinhas, frequência ideal)
- 📋 **Criação de rotinas e cronogramas**
- 🤖 **Personalidade configurada como uma diarista experiente**
- 💬 **Funcionamento por terminal (CLI) com plano de evolução para interface web**

---

## 📆 Google Calendar (funcionalidade removida temporariamente)

A Limpinha foi originalmente desenvolvida com integração ao **Google Calendar**, permitindo o agendamento de faxinas, lembretes e tarefas.

> ⚠️ **Como a API do Google exige verificação para uso público**, a funcionalidade foi **removida temporariamente nesta versão pública**.  
> Você pode visualizar como ela funcionaria no vídeo abaixo.

📺 **[Clique aqui para assistir a demonstração (em breve)](https://www.youtube.com/watch?v=SEU_VIDEO_AQUI)**

---

## 🚀 Como executar localmente

### 🔧 Pré-requisitos

- Python 3.9+
- Uma chave da API do [Gemini IA Studio](https://makersuite.google.com/app)
- Git

---

### 📥 Clone o repositório

```bash
git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
cd NOME_DO_REPOSITORIO

### 🧪 Crie o ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

### 📦 Instale as dependências
pip install -r requirements.txt

### 🔐 Defina a chave da API do Gemini
export GENAI_API_KEY="sua_chave_aqui"     # Linux/macOS
set GENAI_API_KEY=sua_chave_aqui          # Windows

### ▶️ Execute o chatbot
python main.py
