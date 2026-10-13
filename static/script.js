async function askQuestion() {

    const question =
        document.getElementById("question").value;

    const promptType =
        document.getElementById("promptType").value;

    const answerElement =
        document.getElementById("answer");


    if (question.trim() === "") {

        answerElement.textContent =
            "Please enter a question.";

        return;
    }


    answerElement.textContent =
        "Study Assistant is thinking...";


    const response = await fetch("/ask", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            question: question,
            prompt_type: promptType
        })

    });


    const data = await response.json();


    answerElement.textContent =
        data.answer;
}