from flask import Flask, render_template, request
from utils import AI as ai

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_js", methods = ["POST", "GET"])
def get_js():
    data = request.form['rawText']
    newData = ai.compTxt(data)
    return newData

@app.route("/get_bot")
def get_bot_response():
    botText = render_v2py("AI.py", comp)
    return str(render_template("index.html", botText = botText))



if __name__ == "__main__":
    app.run()
