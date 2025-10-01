import sqlite3
from datetime import datetime

DB_FILE = "logs.db"


def log_action(action, triggered_by = "system"):
    "Log gate action to the database"
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO gate_logs (timestamp, action, triggered_by) VALUES (?,?,?)",
              (timestamp, action, triggered_by))
    conn.commit()
    conn.close()

def read_logs(limit=10):
    """Read N logs at a time"""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT timestamp, action, triggered_by FROM gate_logs ORDER BY id DESC LIMIT ?", (limit,))
    rows = c.fetchall()
    conn.close()

    # Convert tuples → list of dicts
    logs = [
        {"timestamp": row[0], "action": row[1], "user": row[2]}
        for row in rows
    ]
    return logs