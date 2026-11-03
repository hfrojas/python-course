texto = input("Ingerese el texto a analizar: ")
texto = texto.lower()
letras = []

letras.append(input("Ingresa la primera letra: ").lower())
letras.append(input("Ingresa la segunda letra: ").lower())
letras.append(input("Ingresa la tercera letra: ").lower())


print("\n")
print("CANTIDAD DE LETRAS")

cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Hemos encontrato {cantidad_letras1} veces la letra {letras[0]}")
print(f"Hemos encontrato {cantidad_letras2} veces la letra {letras[1]}")
print(f"Hemos encontrato {cantidad_letras3} veces la letra {letras[2]}")

print("\n")
print("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en el texto")

print("\n")
print("LETRA INICIAL Y LETRA FINAL")

letra_inicial = texto[0]
letra_final = texto[-1]

print(f"La letra inicial del texto es {letra_inicial}")
print(f"La letra final del texto es {letra_final}")

print("\n")
print("TEXTO INVERTIDO")

texto_invertido = palabras
texto_invertido.reverse()
print(" ".join(texto_invertido))

print("\n")
print("BUSCAR LA PALABRA PYTHON")


buscar_python = "python" in texto
dic = {True: "si", False: "no"}
print(f"la palabra 'python' {dic[buscar_python]} se encuentra en el texto")