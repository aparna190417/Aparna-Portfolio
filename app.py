from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/python-projects")
def python_projects():
    return render_template("python_projects.html")

@app.route("/certificates")
def certificates():
    return render_template("certificates.html")

@app.route("/internship")
def internship():
    return render_template("internship.html")

if __name__ == "__main__":
    app.run(debug=True)

