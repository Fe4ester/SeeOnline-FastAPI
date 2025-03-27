from celery import Celery


app = Celery(
    'SeeOnline',
    broker='pyamqp://guest:guest@localhost//')

app.autodiscover_tasks()
