
from celery import Celery

app = Celery('calc_config', broker='redis://192.168.0.20:6379/0', backend='redis://192.168.0.20:6379', include=['calc', 'calc_mensajes'])
