mi_lista = ["a", "b", "c"]
mi_otra_lista = [4,5,6]
print(type(mi_lista))
print(len(mi_lista))
print(mi_lista[2])
print(mi_lista[::-1])
print(mi_lista + mi_otra_lista)

mi_lista[0]="uno"
print(mi_lista)
mi_otra_lista.append(7)
print(mi_otra_lista)
elemento_eliminado = mi_otra_lista.pop()
print(mi_otra_lista)
print(elemento_eliminado)

letras = ["G", "O", "B", "M", "C"]
print(letras)
letras.sort()
print(letras)
letras.reverse()
print(letras)
