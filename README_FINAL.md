# 🧼 Limpinha – Chatbot para Diaristas e Tarefas Domésticas

> **Uma aliada virtual para quem cuida da casa. Feita com carinho, sabão e tecnologia.**

![QR Code do Projeto](docs/qrcode.png)

---

**Limpinha** é uma assistente virtual criada especialmente para atender **donas de casa, diaristas, aposentadas e pessoas que lidam com a rotina doméstica**, muitas vezes invisibilizadas pela tecnologia tradicional.

Ela traz leveza, bom humor e conhecimento prático para ajudar em tarefas do lar: desde como limpar manchas difíceis até montar uma rotina semanal de organização.

Este projeto nasceu de uma **competição de chatbots** com o propósito de causar impacto real em comunidades que muitas vezes são deixadas de lado pelas inovações digitais.

---

## ✨ Funcionalidades

- 💬 Conversa com linguagem **simples, empática e bem-humorada**
- 🧽 **Dicas de limpeza** com produtos caseiros ou comerciais
- 📅 **Sugestões de rotina doméstica** e cronogramas de faxina
- 📚 **Respostas rápidas para dúvidas comuns sobre o lar**
- 🎙️ **Entrada por voz** com transcrição automática em tempo real
- 📱 Interface **moderna e adaptada** para celulares e navegadores

---

## ❌ Google Calendar (atualmente desativado)

> Este projeto originalmente **permitia agendar faxinas diretamente no Google Agenda** por voz ou texto.

Entretanto, por limitações de tempo e a exigência de **verificação do Google para apps públicos**, a funcionalidade foi **temporariamente removida desta versão**. Uma atualização próxima poderá reativar esse recurso.

---

## 🖼️ Interface visual

Abaixo, algumas imagens reais da próxima implementação com google agenda/calendário



---

## 🚀 Teste agora

Você pode testar a Limpinha diretamente no navegador pelo link abaixo:

🔗 **https://limpinha.onrender.com**  
_(ou escaneie o QR Code no topo deste documento)_

---

## 🧪 Executar localmente (para desenvolvedores)

### 🔧 Pré-requisitos

- Python 3.9+
- Uma chave da API do [Gemini IA Studio]
- Git

---

### 📥 Clone o repositório

```bash
git clone https://github.com/seu-usuario/limpinha.git
cd limpinha
```

### 🧪 Crie o ambiente virtual (opcional)

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 📦 Instale as dependências

```bash
pip install -r requirements.txt
```

### 🔐 Configure a chave da API (usando variável de ambiente)

```bash
export GENAI_API_KEY="sua_chave_aqui"       # macOS/Linux
set GENAI_API_KEY=sua_chave_aqui            # Windows
```

---

### ▶️ Inicie o servidor

```bash
python main.py
```

---

## ❤️ Feito com carinho

Criado por Arthur Malveste, com dedicação para valorizar quem cuida da casa com tanta responsabilidade.
