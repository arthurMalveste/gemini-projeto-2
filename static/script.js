function enviarMensagem() {
    const input = document.getElementById("mensagem");
    const texto = input.value.trim();
    if (!texto) return;
  
    exibirMensagem("Você", texto, "text-right text-blue-700 bg-blue-100");
  
    input.value = "";
  
    fetch("/responder", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ mensagem: texto })
    })
      .then(res => res.json())
      .then(data => {
        exibirMensagem("Limpinha", data.resposta, "text-left text-yellow-800 bg-yellow-100");
      });
  }
  
  function exibirMensagem(remetente, texto, classeExtra) {
    const chat = document.getElementById("chat");
    const msg = document.createElement("div");
    msg.className = `p-2 rounded-lg my-2 ${classeExtra}`;
    msg.innerHTML = `<strong>${remetente}:</strong> ${texto}`;
    chat.appendChild(msg);
    chat.scrollTop = chat.scrollHeight;
  }
  
// Função chamada ao enviar a mensagem
function enviarMensagem() {
    const input = document.getElementById("mensagem");
    const texto = input.value.trim();
    if (!texto) return;
  
    exibirMensagem("Você", texto, "text-right text-blue-700 bg-blue-100");
    input.value = "";
  
    fetch("/responder", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ mensagem: texto })
    })
    .then(res => res.json())
    .then(data => {
      exibirMensagem("Limpinha", data.resposta, "text-left text-yellow-800 bg-yellow-100");
    });
  }
  
  // Exibe mensagens no chat
  function exibirMensagem(remetente, texto, classeExtra) {
    const chat = document.getElementById("chat");
    const msg = document.createElement("div");
    msg.className = `p-2 rounded-lg my-2 ${classeExtra}`;
    msg.innerHTML = `<strong>${remetente}:</strong> ${texto}`;
    chat.appendChild(msg);
    chat.scrollTop = chat.scrollHeight;
  }
  
  // Adiciona funcionalidade ao pressionar "Enter"
  document.addEventListener("DOMContentLoaded", () => {
    const input = document.getElementById("mensagem");
  
    input.addEventListener("keydown", function (event) {
      if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault(); // Impede quebra de linha
        enviarMensagem();
      }
    });
  });
  
  function usarSugestao(texto) {
    const input = document.getElementById("mensagem");
    input.value = texto;
    enviarMensagem();
  }
    