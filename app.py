from flask import Flask, render_template, request

app = Flask(__name__)

faq = {
    "what is python": "Python is a popular programming language.",
    "what is flask": "Flask is a lightweight Python web framework.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "who developed python": "Python was developed by Guido van Rossum.",
    "what is machine learning": "Machine Learning is a branch of AI."
}

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""

    if request.method == "POST":
        user_question = request.form["question"].lower()

        if user_question in faq:
            response = faq[user_question]
        else:
            response = "Sorry, I don't know the answer."

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)