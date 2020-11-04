import calc
import calc_mensajes
import time

n1 = int(input("Ingrese un valor: "))
n2 = int(input("Ingrese otro valor: "))
r = calc.suma.delay(n1,n2)
time.sleep(1)
if r.ready():
    print("La suma es : %d" % r.get())
