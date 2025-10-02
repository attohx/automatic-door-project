import sqlite3 
import flask
import config
 
app = flask.Flask(__name__)

#connect or create database
def kreatedb():
    conn = sqlite3.connect('logs.db')
    c = conn.cursor()
    c.execute("""

        CREATE TABLE IF NOT EXISTS gate_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            action TEXT,
            triggered_by TEXT
        )
        """)
    
    c.execute("""
    CREATE TABLE IF NOT EXISTS schedule (
        id INTEGER PRIMARY KEY CHECK (id = 1),
        open_time TEXT,   -- format "HH:MM"
        close_time TEXT   -- format "HH:MM"
    )
    """)
    
    
    # insert default schedule if none exists
    c.execute("SELECT COUNT(*) FROM schedule")
    count = c.fetchone()[0]
    if count == 0:
        # use config.SCHEDULE fallback
        open_hour = int(config.SCHEDULE.get("OPEN_HOUR", 6))
        close_hour = int(config.SCHEDULE.get("CLOSE_HOUR", 19))
        open_time = f"{open_hour:02d}:00"
        close_time = f"{close_hour:02d}:00"
        c.execute("INSERT INTO schedule (id, open_time, close_time) VALUES (1, ?, ?)",
                  (open_time, close_time))
        
    conn.commit()
    conn.close()
    print ("Database Created succesfully!")