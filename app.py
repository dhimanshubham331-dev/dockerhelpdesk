
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

import os

os.makedirs("/app/data", exist_ok=True)
DATABASE = "/app/data/helpdesk.db"


# Connect to database
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# Create ticket table
def init_db():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee TEXT NOT NULL,
            issue TEXT NOT NULL,
            description TEXT NOT NULL,
            status TEXT DEFAULT 'Pending'
        )
    """)

    conn.commit()
    conn.close()


# Home page
@app.route("/")
def home():
    conn = get_db()

    tickets = conn.execute(
        "SELECT * FROM tickets ORDER BY id DESC"
    ).fetchall()

    conn.close()

    return render_template("index.html", tickets=tickets)


# Submit ticket
@app.route("/create", methods=["POST"])
def create_ticket():

    employee = request.form["employee"]
    issue = request.form["issue"]
    description = request.form["description"]

    conn = get_db()

    conn.execute(
        "INSERT INTO tickets (employee, issue, description) VALUES (?, ?, ?)",
        (employee, issue, description)
    )

    conn.commit()
    conn.close()

    return redirect("/")


# Update ticket
@app.route("/update/<int:ticket_id>", methods=["POST"])
def update_ticket(ticket_id):

    status = request.form["status"]

    if status not in ["Pending", "In Progress", "Resolved"]:
        return "Invalid status", 400

    conn = get_db()

    conn.execute(
        "UPDATE tickets SET status = ? WHERE id = ?",
        (status, ticket_id)
    )

    conn.commit()
    conn.close()

    return redirect("/")


init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
