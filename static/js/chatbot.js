function sendMsg() {
    const msgInput = document.getElementById("msg");
    const replyBox = document.getElementById("chat-reply");

    fetch("/chat/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: msgInput.value })
    })
        .then(res => res.json())
        .then(data => {
            replyBox.classList.remove("d-none");
            replyBox.innerText = data.reply;
            msgInput.value = "";
        });
}
