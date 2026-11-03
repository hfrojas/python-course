from shlex import join

texto = "Este es el texto de Federico"
resultado = texto

print(resultado.upper())
print(resultado[2:8].upper())
print(resultado.lower())
print(resultado.split())
print(resultado.split("t"))

a = "Aprender"
b = "Python"
c = "es"
d = "genial"

union = "-".join([a, b, c, d])
print(union)
print(resultado.find("g"))
print(resultado.find("text"))
print(resultado.replace("Federico","Harold"))