#La listas puede guardar diferentes tipos de datos a diferencia de otros lenguajes.
lista = ["Java", "Python", "C#", True, 23, "Ruby", None, False, 7]
print(lista)
lista.append("PHP")
print(lista)
lista.insert(2, "Javascript")
print(lista)
lista.reverse()
print(lista)
#not supported between instances of 'int' and 'str' pero de un solo tipo si ordena
#lista.sort()
lista.pop(3)
print(lista)
lista.remove(False)
print(lista)
print(lista.count('Java'))
lista[1] = 'Visual Basic'
lista[3] = "Go!"
lista.remove(True)
print(lista)
lista.sort()
print(lista)
print(len(lista))

lista = [1,2,3,4,5]
lista2 = lista[-3:]
print(lista2)