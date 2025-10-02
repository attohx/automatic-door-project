import sqlite3

DB_FILE = "settings.db"

def init_settings_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS settings (
            id INTEGER PRIMARY KEY,
            key TEXT UNIQUE,
            value TEXT
        )
    """)
    conn.commit()
    conn.close()

def set_location(city):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)", ("location", city))
    conn.commit()
    conn.close()

def get_location():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT value FROM settings WHERE key = ?", ("location",))
    row = c.fetchone()
    conn.close()
    return row[0] if row else "Accra"
