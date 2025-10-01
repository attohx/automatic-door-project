import sqlite3

DB_FILE = "logs.db"

def init_schedule_db():
    """Create schedule table if it doesn’t exist"""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS schedule (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            open_time TEXT,
            close_time TEXT
        )
    """)
    # Ensure one row exists
    c.execute("SELECT COUNT(*) FROM schedule")
    if c.fetchone()[0] == 0:
        c.execute("INSERT INTO schedule (open_time, close_time) VALUES (?, ?)", ("06:00", "18:00"))
    conn.commit()
    conn.close()

def get_schedule():
    """Return the current schedule row"""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT open_time, close_time FROM schedule ORDER BY id DESC LIMIT 1")
    row = c.fetchone()
    conn.close()
    if row:
        return {"open_time": row[0], "close_time": row[1]}
    return None

def update_schedule(open_time, close_time):
    """Update schedule row"""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    # Replace existing row with new values
    c.execute("DELETE FROM schedule")
    c.execute("INSERT INTO schedule (open_time, close_time) VALUES (?, ?)", (open_time, close_time))
    conn.commit()
    conn.close()
