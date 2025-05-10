from flask import Flask, request, render_template, redirect, url_for
from model_For_Rag import classify_query_with_chroma

app = Flask(__name__)

chat_history = []

@app.route("/", methods=["GET", "POST"])
def index():
    global chat_history
    if request.method == "POST":
        user_input = request.form["query"]
        route =  classify_query_with_chroma(user_input, top_k=3)  # Replace with real response later
        bot_reply = f"Route for this Query: {str(route).upper()}"
        chat_history.append(("user", user_input))
        chat_history.append(("bot", bot_reply))
        return redirect(url_for("index"))
    return render_template("chat.html", chat_history=chat_history)

if __name__ == "__main__":
    app.run(debug=True)
