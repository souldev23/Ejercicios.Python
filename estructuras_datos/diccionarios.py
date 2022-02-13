dic = {1:"Mu", 2: "Aldebarán", 3: "Saga"}

print(dic)
print(dic[2])
#Si la Key no existe y se usan corchetes generará error, para eso se puede usar get print(dic[4])X dic.get(4)V
print(dic.get(3), dic.get(4))
dic = {"Aries":"Mu", "Tauro": "Aldebarán", "Géminis": "Saga"}
print(dic)
print(dic["Aries"])
print(dic.get("Géminis"))
for elemento in dic:
    print(elemento)
    print(dic[elemento])

print(dic.keys())
print(dic.values())
print(dic.items())
dic["Géminis"] = "Kanon"
print(dic)
dic["Cáncer"] = "Death Mask"
print(dic)
print(dic.setdefault("Capricornio", "Shura"))
print(dic)
print(dic.pop("Capricornio"))
print(dic)