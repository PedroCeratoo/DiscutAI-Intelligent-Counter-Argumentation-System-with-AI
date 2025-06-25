const chatHistory = [];

async function sendMessage() {
  const input = document.getElementById('userInput');
  const chatBox = document.getElementById('chatBox');
  const messageText = input.value.trim();

  if (messageText !== '') {
    const userMessage = document.createElement('div');
    userMessage.classList.add('message', 'user');
    userMessage.textContent = messageText;
    chatBox.appendChild(userMessage);

    input.value = '';
    chatBox.scrollTop = chatBox.scrollHeight;

    const loadingMessage = document.createElement('div');
    loadingMessage.classList.add('message', 'bot');
    loadingMessage.innerHTML = 'DiscutAI está digitando <span class="loading"></span>';
    chatBox.appendChild(loadingMessage);
    chatBox.scrollTop = chatBox.scrollHeight;

    try {
      const response = await fetch('http://localhost:8000/api/debate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          mensagem: messageText,
          historico: chatHistory
        })
      });

      const data = await response.json();
      loadingMessage.remove();

      const botMessage = document.createElement('div');
      botMessage.classList.add('message', 'bot');
      botMessage.textContent = data.resposta || 'Erro ao processar a resposta.';
      chatBox.appendChild(botMessage);
      chatBox.scrollTop = chatBox.scrollHeight;

      chatHistory.push(
        { aluno: messageText },
        { discutai: data.resposta }
      );

    } catch (error) {
      loadingMessage.remove();

      const botMessage = document.createElement('div');
      botMessage.classList.add('message', 'bot');
      botMessage.textContent = 'Erro ao conectar com o servidor.';
      chatBox.appendChild(botMessage);
      chatBox.scrollTop = chatBox.scrollHeight;
    }
  }
}

document.getElementById('userInput').addEventListener('keydown', function (event) {
  if (event.key === 'Enter') {
    sendMessage();
  }
});
