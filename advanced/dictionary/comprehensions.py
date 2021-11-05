def cubo():
    cube_dict = {i: i**3 for i in range(1, 101) if(i % 3 != 0)}
    return cube_dict

def raiz():
    squirt_dict = {i:round(i**0.5,2) for i in range(1, 1001)}
    return squirt_dict

def run():
    print("Cubos: ", cubo())
    print("Mil raices: ", raiz())

if __name__ == '__main__':
    run()