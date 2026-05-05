from flask import Flask, render_template, request, redirect, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"


# ================= DATABASE INIT =================
def init_db():
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        message TEXT
    )
    """)

    conn.commit()
    conn.close()


# ================= HOME =================
@app.route("/")
def home():
    return render_template("index.html")


# ================= PROJECTS =================
@app.route("/projects")
def projects():
    return render_template("projects.html")


# ================= CERTIFICATES =================
@app.route("/certificates")
def certificates():
    return render_template("certificates.html")


# ================= INTERNSHIP =================
@app.route("/internship")
def internship():
    return render_template("internship.html")


# ================= BLOG =================
@app.route("/blog")
def blog():
    return render_template("blog.html")

# ================= ADMIN =================
@app.route("/admin")
def admin():
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM messages")
    data = cursor.fetchall()

    conn.close()

    return render_template("admin.html", messages=data)

# ================= CONTACT FORM =================
@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    print(name, email, message)   # ✅ yaha hona chahiye

    try:
        conn = sqlite3.connect("messages.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO messages (name, email, message) VALUES (?, ?, ?)",
            (name, email, message)
        )

        conn.commit()
        conn.close()

        print("✅ Message saved in DB")

    except Exception as e:
        print("❌ DB error:", e)

    flash("✅ Message saved successfully!")
    return redirect("/")


# ================= RUN =================
if __name__ == "__main__":
    init_db()   # 👈 FIRST RUN pe table create karega
    app.run(debug=True)