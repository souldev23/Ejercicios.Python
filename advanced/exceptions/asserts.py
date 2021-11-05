def get_multiples(num):
    multiples = [i for i in range(1, num + 1) if (num % i == 0)]
    return multiples

def run():
    try:
        num = input('Ingrese el número del cual desee obtener sus multiplos \n')
        assert num.isnumeric(), "El elemento ingresado no es un número."
        num = int(num)
        if(num < 1):
            raise 'Menor a 1'
        print(get_multiples(num))
    except:
        if(TypeError):
            print('El número debe ser un entero positivo mayor a 0.')
        else:
            print('Ocurrió un error desconocido.')


if __name__ == '__main__':
    run()