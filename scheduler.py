# scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import schedule_db
import state
import logs_db
from mail import send_email
from config import TO_EMAIL

scheduler = BackgroundScheduler()

def open_gate_task(app):
    with app.app_context():
        if state.get_state() != "OPEN":
            state.set_state("OPEN")
            logs_db.log_action("OPENED", "scheduler")
            try:
                send_email("Poultry Gate Opened ⏰", 
                           "The gate was automatically opened by schedule.", 
                           [TO_EMAIL])
            except Exception as e:
                print("Error sending scheduled open email:", e)

def close_gate_task(app):
    with app.app_context():
        if state.get_state() != "CLOSED":
            state.set_state("CLOSED")
            logs_db.log_action("CLOSED", "scheduler")
            try:
                send_email("Poultry Gate Closed ⏰", 
                           "The gate was automatically closed by schedule.", 
                           [TO_EMAIL])
            except Exception as e:
                print("Error sending scheduled close email:", e)

def schedule_jobs(app):
    """Read schedule from DB and create jobs."""
    sched = schedule_db.get_schedule()
    if not sched:
        return

    open_hour, open_min = map(int, sched["open_time"].split(":"))
    close_hour, close_min = map(int, sched["close_time"].split(":"))

    scheduler.add_job(open_gate_task, 
                      trigger=CronTrigger(hour=open_hour, minute=open_min),
                      args=[app],
                      id="open_job",
                      replace_existing=True,
                      max_instances=1)

    scheduler.add_job(close_gate_task,
                      trigger=CronTrigger(hour=close_hour, minute=close_min),
                      args=[app],
                      id="close_job",
                      replace_existing=True,
                      max_instances=1)

def init_scheduler(app):
    """Initialize and start the scheduler with jobs."""
    if not scheduler.running:
        scheduler.start()
    schedule_jobs(app)
    return scheduler
