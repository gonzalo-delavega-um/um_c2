# An example python program using semaphore provided by the python multiprocessing module

import multiprocessing
import time


def EntraAuto(slots,entra,entraL):
        slots.acquire()
        entraL.acquire()
        entra.value = entra.value+1
        entraL.release()
        print(">>>>> Entrando auto: %d" % (entra.value))

def SaleAuto(slots,sale,saleL):
        slots.release()
        saleL.acquire()
        sale.value = sale.value+1
        saleL.release()
        print("<<<<< Saliendo auto: %d" % (sale.value))

# Process that simulates the entry of cars into the parking lot
def entrando(slots,entra, entraL):
    # Creates multiple threads inside to simulate cars that are entra
    while(True):
        time.sleep(1)
        incomingCar = multiprocessing.Process(target=EntraAuto, args=(slots,entra,entraL))
        incomingCar.start()
        incomingCar.join()
        print("------------------------------------> Entró auto! Slots: %d" % slots.get_value())

# Process that simulates the exit of cars from the parking lot
def saliendo(slots,sale, saleL):
    # Creates multiple threads inside to simulate cars taken out from the parking lot
    while(True):
        time.sleep(3)
        outgoingCar = multiprocessing.Process(target=SaleAuto, args=(slots,sale,saleL))
        outgoingCar.start()
        outgoingCar.join()
        print("------------------------------------> Salio auto! Slots: %d" % slots.get_value())


if __name__=="__main__":
    # Start the parking eco-system
    entra = multiprocessing.Value('d', 0)
    sale = multiprocessing.Value('d', 0)

    slots = multiprocessing.Semaphore(10)
    entraL = multiprocessing.Lock()
    saleL = multiprocessing.Lock()
   

    print("Slots iniciales: %d" % slots.get_value())
    entraProc = multiprocessing.Process(target=entrando, args=(slots,entra, entraL))
    saleProc = multiprocessing.Process(target=saliendo, args=(slots,sale, saleL))
    entraProc.start()
    saleProc.start()
