from conversion import dolar_a_peso, euro_a_peso

tasa_de_cambio_dolar = 4000
tasa_de_cambio_euro = 4500

print("Seleccione la opción de conversión:")
print("1. Convertir de USD a Pesos")
print("2. Convertir de EUR a Pesos")

opcion = int(input("Ingrese el número de la opción elegida: "))

if opcion == 1:
    monto = float(input("Ingrese el monto en USD: "))
    resultado = dolar_a_peso(monto, tasa_de_cambio_dolar)
    print(f"{monto} USD equivale a {resultado} Pesos.")
elif opcion == 2:
    monto = float(input("Ingrese el monto en EUR: "))
    resultado = euro_a_peso(monto, tasa_de_cambio_euro)
    print(f"{monto} EUR equivale a {resultado} Pesos.")
else:
    print("Opción no válida.")
