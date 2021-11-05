lista = [1, 2, 3, 4, 5]

def run():
    cuadrados = list(map(lambda x: x**2, lista))
    print(cuadrados)

if __name__ == '__main__':
    run()