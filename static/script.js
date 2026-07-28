const button = document.getElementById("speak");

button.onclick = function () {

    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();

    recognition.lang = "en-US";
    recognition.start();

    recognition.onresult = function (event) {

        let text = event.results[0][0].transcript;

        document.getElementById("user").innerHTML = "You : " + text;

        fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: text
            })
        })
        .then(response => response.json())
        .then(data => {

            document.getElementById("bot").innerHTML = "Bot : " + data.reply;

            let speech = new SpeechSynthesisUtterance(data.reply);
            speech.lang = "en-US";
            window.speechSynthesis.speak(speech);

        })
        .catch(error => {
            console.log(error);
        });

    };

};
