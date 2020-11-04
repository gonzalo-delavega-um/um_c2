
from celery import Celery

app = Celery('calc_monolitico', broker='redis://192.168.0.10:6379', backend='redis://192.168.0.10:6379')

@app.task
def suma(a, b):
    return a+b

@app.task
def resta(a, b):
    return a-b

@app.task
def mult(a, b):
    return a*b

@app.task
def div(a, b):
    if b!=0:
        return a/b
    return 0

if __name__ == '__main__':
    r = suma.delay(2,3)
    print(r.get())
