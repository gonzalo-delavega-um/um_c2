
from celery import Celery
import os

app = Celery('tasks', broker='redis://localhost', backend='redis://localhost:6379')

@app.task
def add(x, y):
    return x + y

@app.task
def mipid():
    return os.getpid()

if __name__ == "__main__":
    app.start()
