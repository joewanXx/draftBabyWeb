from flask import Flask, jsonify, redirect,  url_for, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Corps Manager',
        'location': 'Tondo, Manila',
        'salary': 'PHP 30,000'
    },
    {
        'id': 2,
        'title': 'Taga-timbang',
        'location': 'Majayjay, Laguna',
        'salary': 'PHP 25,000'
    },
    {
        'id': 3,
        'title': 'Contractor',
        'location': 'Tondo, Manila',
        'salary': 'PHP 3,000,000,000'
    },
    {
        'id': 4,
        'title': 'Congressman',
        'location': 'Majayjay, Laguna',
        'salary': 'PHP 6,000,000,000'
    },
    {
        'id': 5,
        'title': 'Saging Smasher',
        'location': 'Vancouver, Canada',
        'salary': 'PHP 10'
    }
]

@app.route("/")
def home():
    return render_template("index.html",
                           jobs=JOBS,
                           company_name='Johan Tambay Society')

@app.route("/api/jobs")
@app.route("/nya")
def jobs_list():
    return jsonify(JOBS)

@app.route("/jepoydizon")
def meme():
    return render_template("user.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/prof")
def prof():
    return render_template("myprofile.html")

# @app.route("/<name>")
# def user(name):
#     return render_template("index.html", content=name, tt="pakiss naman oh!")



if __name__ == "__main__":
    app.run(debug=True)