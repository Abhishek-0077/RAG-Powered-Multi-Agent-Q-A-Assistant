from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

chat_history = []

@app.route("/", methods=["GET", "POST"])
def index():
    global chat_history
    if request.method == "POST":
        user_input = request.form["query"]
        bot_reply = "OK"  # Replace with real response later
        chat_history.append(("user", user_input))
        chat_history.append(("bot", bot_reply))
        return redirect(url_for("index"))
    return render_template("chat.html", chat_history=chat_history)

if __name__ == "__main__":
    app.run(debug=True)
