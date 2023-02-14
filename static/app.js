const chatHistory = document.getElementById("chat-history");

    const chatForm = document.getElementById("chat-form");

    const messageInput = document.getElementById("message");

 

    chatForm.addEventListener("submit", (event) => {

      event.preventDefault();

      const message = messageInput.value;

      messageInput.value = "";

      addChatBubble(message, true);

     fetch('http://localhost:5000/api/send-message', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Origin': 'http://localhost:63342'
  },
  body: JSON.stringify({ message: 'Hello, world!' })
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch((error) => console.error(error));

    });

 

    function addChatBubble(text, isUser) {

      const chatBubble = document.createElement("div");

      chatBubble.classList.add("chat-bubble");

      if (isUser) {

        chatBubble.classList.add("user");

      }

      chatBubble.textContent = text;

      chatHistory.appendChild(chatBubble);

      chatHistory.scrollTop = chatHistory.scrollHeight;

    }
