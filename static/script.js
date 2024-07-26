document.addEventListener("DOMContentLoaded", function() {
    // Add event listener for "Enter" key
    document.getElementById("user-input").addEventListener("keydown", function(event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    });
});

function sendMessage() {
    var userMessage = document.getElementById("user-input").value;
    if (userMessage.trim() === "") return; // Don't send empty messages
    displayMessage(userMessage, true);
    document.getElementById("user-input").value = "";
    
    fetch('http://localhost:5005/webhooks/rest/webhook', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userMessage })
    })
    .then(response => response.json())
    .then(data => {
        if (data && data.length > 0) {
            var botResponse = data[0].text; // Extract first response from Rasa
            displayMessage(botResponse, false);
        }
    })
    .catch(error => console.error('Error:', error));
}

function displayMessage(message, isUser) {
    var chatDisplay = document.getElementById("chat-display");
    var messageElement = document.createElement("div");
    messageElement.textContent = message;
    messageElement.className = isUser ? "user-message" : "bot-message";
    chatDisplay.appendChild(messageElement);
    chatDisplay.scrollTop = chatDisplay.scrollHeight; // Auto scroll to bottom
}

