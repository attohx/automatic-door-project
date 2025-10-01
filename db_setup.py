import sqlite3 
import flask
 
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
    conn.commit()
    conn.close()
    print ("Database Created succesfully!")