import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("python_projects.html")

@app.route("/certificates")
def certificates():
    return render_template("certificates.html")

@app.route("/internship")
def internship():
    return render_template("internship.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))