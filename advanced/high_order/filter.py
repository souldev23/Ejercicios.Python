lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def run():
    impares = list(filter(lambda x: x % 2 != 0, lista))
    pares = list(filter(lambda x: x % 2 == 0, lista))
    print(impares)
    print(pares)

if __name__ == '__main__':
    run()