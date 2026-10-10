nombre = input("Nombre del vendedor:")
ventas = float(input("ventas realizadas:"))

print(f"{nombre} tiene {ventas} ventas")
comision = round((ventas * 13) / 100,2)
print(f"{nombre} tiene {comision} comision")