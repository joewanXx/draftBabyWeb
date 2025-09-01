from flask import Flask, redirect,  url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/jepoydizon")
def meme():
    return render_template("user.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/<name>")
def user(name):
    return render_template("index.html", content=name, tt="pakiss naman oh!")

if __name__ == "__main__":
    app.run(debug=True)