from apscheduler.schedulers.background import BackgroundScheduler
from django.core.mail import send_mail


def task():
    pass


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(task, 'interval', minutes=1)
    scheduler.start()
