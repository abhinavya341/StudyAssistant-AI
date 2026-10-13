from flask import Flask, render_template, request, jsonify
from assistant import answer_question

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()

    question = data.get("question", "").strip()
    prompt_type = data.get("prompt_type", "zero-shot")

    if not question:
        return jsonify({
            "answer": "Please enter a question."
        })

    answer = answer_question(question, prompt_type)

    return jsonify({
        "answer": answer,
        "prompt_type": prompt_type
    })


if __name__ == "__main__":
    app.run(debug=True)