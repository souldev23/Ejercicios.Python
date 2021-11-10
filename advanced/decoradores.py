from datetime import datetime as dt
from typing import List

def mayus(func):
    def wrapper(msg: str) -> str:
        return func(msg.upper())
    return wrapper

#Función que calcula el tiempo de ejecución
def excecution_time(my_func):
    def my_wrapper(*args, **kwargs): #*args, **kwargs indica que no importa el número de argumentos si son parametros posicionales o no
        suma = 0
        init_time = dt.now()
        suma = my_func(*args, **kwargs)
        end_time = dt.now()
        elapsed_time = end_time - init_time
        return "El resultado de la suma es: " + str(suma) + "\nTranscurrieron " + str(round(elapsed_time.total_seconds(), 3)) + " segundos."
    return my_wrapper

@excecution_time
def suma(a: int, b: int) -> int:    
    return a + b

@mayus
def message_received(msg: str) -> str:
    return "Recibiste un mensaje:\n"+ msg

def run():
    #print(message_received("Que pedo con esto?, está bien loco!"))
    print(suma(974893743343,59283734892))
    

if __name__ == '__main__':
    run()