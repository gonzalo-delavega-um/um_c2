
from calc_config import app
import time

@app.task
def saludo():
    time.sleep(5)
    return "Hola Mundo, calculadora reportando..."
