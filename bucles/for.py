def run():
    for i in range(1, 11):
        print(i)
    for c in "Hola mundo!":
        print(c)
    lista = ["Java", "Python", "C#", True, 23, "Ruby", None, False, 7]
    for elemento in lista:
        if (elemento == "C#"):
            continue
        elif (not elemento):
            break
        print(elemento)

if __name__ == '__main__':
    run()