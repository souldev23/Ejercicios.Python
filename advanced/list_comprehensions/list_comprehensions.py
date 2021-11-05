def run():
    # Agrega a la lista solo los números que son multiplos de 4, 6 y 9
    lista = [i for i in range (1, 100) if (i % 4 == 0 or i % 6 == 0 or i % 9 == 0)]
    print(lista)
    # Obtenemos solo pares de la lista anterior
    lista2 = [i for i in lista if i % 2 == 0]
    print(lista2)

if __name__ == '__main__':
    run()