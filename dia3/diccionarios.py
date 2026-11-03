#"clave": "valor"
diccionario = {"clave": "valor", "nombre": "nombre"}
print(type(diccionario))
print(diccionario)
print(diccionario["clave"])
print(diccionario["nombre"])

cliente = {"nombre": "juan", "apellido": "fuentes", "edad":25, "peso": 70, "talla": 1.76}
print(cliente)
print(cliente["apellido"])

dic = {"c1": 55, "c2": [10,20,30], "c3":{"s1":100, "s2":200}}
print(dic["c2"][1])
print(dic["c3"]["s2"])

dic["c4"] = "cuantos"
print(dic.keys())
print(dic.values())
print(dic.items())

