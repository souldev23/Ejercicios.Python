# Es una estructura de datos inmutable
tupla = ("Java", "Python", "C#", True, 23, "Ruby", "C#", False, 7)

print(tupla.count("C#"))
print(tupla.index("Python"))

for elemento in tupla:
    print(elemento)

lista = []
for i in range(1,11):
    lista.append(i)

tupla = tuple(lista)
print(lista)
print(tupla)