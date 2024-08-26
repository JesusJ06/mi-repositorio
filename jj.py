import getpass

usuarios = {
    "usuario1": {"contraseña": "1234", "saldo": 1000},
    "usuario2": {"contraseña": "5678", "saldo": 500}
}

def inicio_sesion():
    """Función para iniciar sesión"""
    usuario = input("Ingrese su usuario: ")
    contraseña = getpass.getpass("Ingrese su contraseña: ")

    if usuario in usuarios and usuarios[usuario]["contraseña"] == contraseña:
        return usuario
    else:
        print("Usuario o contraseña incorrectos")
        return None

def consulta_saldo(usuario):
    """Función para consultar el saldo"""
    print(f"Su saldo actual es: {usuarios[usuario]['saldo']}")

def retiro_efectivo(usuario):
    """Función para retirar efectivo"""
    cantidad = int(input("Ingrese la cantidad a retirar: "))

    if cantidad <= usuarios[usuario]["saldo"]:
        usuarios[usuario]["saldo"] -= cantidad
        print(f"Retiro exitoso. Su nuevo saldo es: {usuarios[usuario]['saldo']}")
    else:
        print("No tiene suficiente saldo para realizar el retiro")

def deposito_efectivo(usuario):
    """Función para depositar efectivo"""
    cantidad = int(input("Ingrese la cantidad a depositar: "))

    usuarios[usuario]["saldo"] += cantidad
    print(f"Depósito exitoso. Su nuevo saldo es: {usuarios[usuario]['saldo']}")

def main():
    """Función principal"""
    print("Bienvenido al cajero automático")

    usuario = inicio_sesion()

    if usuario:
        while True:
            print("\nOpciones:")
            print("1. Consultar saldo")
            print("2. Retirar efectivo")
            print("3. Depositar efectivo")
            print("4. Salir")

            opcion = input("Ingrese su opción: ")

            if opcion == "1":
                consulta_saldo(usuario)
            elif opcion == "2":
                retiro_efectivo(usuario)
            elif opcion == "3":
                deposito_efectivo(usuario)
            elif opcion == "4":
                print("Gracias por utilizar nuestro cajero automático")
                break
            else:
                print("Opción inválida. Por favor, inténtelo de nuevo")

if __name__ == "__main__":
    main()