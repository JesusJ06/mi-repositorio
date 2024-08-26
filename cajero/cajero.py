class Cuenta:
    def __init__(self, numero_cuenta, pin, saldo_inicial=0):
        self.numero_cuenta = numero_cuenta
        self.pin = pin
        self.saldo = saldo_inicial
        self.historial = []

    def consultar_saldo(self):
        print(f"Su saldo actual es: ${self.saldo:.2f}")
        self.historial.append(f"Consulta de saldo: ${self.saldo:.2f}")

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Has depositado ${monto:.2f}. Su nuevo saldo es: ${self.saldo:.2f}")
            self.historial.append(f"Depósito: ${monto:.2f}")
        else:
            print("El monto a depositar debe ser mayor que 0.")

    def retirar(self, monto):
        if monto > self.saldo:
            print("Fondos insuficientes.")
        elif monto <= 0:
            print("El monto a retirar debe ser mayor que 0.")
        else:
            self.saldo -= monto
            print(f"Has retirado ${monto:.2f}. Su nuevo saldo es: ${self.saldo:.2f}")
            self.historial.append(f"Retiro: ${monto:.2f}")

    def transferir(self, monto, cuenta_destino):
        if monto > self.saldo:
            print("Fondos insuficientes para transferir.")
        elif monto <= 0:
            print("El monto a transferir debe ser mayor que 0.")
        else:
            self.saldo -= monto
            cuenta_destino.saldo += monto
            print(f"Has transferido ${monto:.2f} a la cuenta {cuenta_destino.numero_cuenta}.")
            self.historial.append(f"Transferencia a {cuenta_destino.numero_cuenta}: ${monto:.2f}")
            cuenta_destino.historial.append(f"Transferencia recibida de {self.numero_cuenta}: ${monto:.2f}")

    def mostrar_historial(self):
        print("\n--- Historial de Transacciones ---")
        if not self.historial:
            print("No hay transacciones en el historial.")
        else:
            for transaccion in self.historial:
                print(transaccion)


class CajeroAutomatico:
    def __init__(self):
        self.cuentas = {}

    def agregar_cuenta(self, numero_cuenta, pin, saldo_inicial=0):
        if numero_cuenta in self.cuentas:
            print("El número de cuenta ya existe.")
        else:
            self.cuentas[numero_cuenta] = Cuenta(numero_cuenta, pin, saldo_inicial)
            print(f"Cuenta {numero_cuenta} creada exitosamente con saldo inicial de ${saldo_inicial:.2f}.")

    def autenticar_usuario(self):
        numero_cuenta = input("Ingrese su número de cuenta: ")
        pin = input("Ingrese su PIN: ")

        cuenta = self.cuentas.get(numero_cuenta)
        if cuenta and cuenta.pin == pin:
            print("Autenticación exitosa.")
            return cuenta
        else:
            print("Número de cuenta o PIN incorrectos.")
            return None

    def mostrar_menu(self):
        print("\n--- Cajero Automático ---")
        print("1. Consultar Saldo")
        print("2. Depositar Dinero")
        print("3. Retirar Dinero")
        print("4. Transferir Dinero")
        print("5. Ver Historial de Transacciones")
        print("6. Salir")

    def ejecutar(self):
        print("Bienvenido al Cajero Automático.")
        while True:
            cuenta = self.autenticar_usuario()
            if cuenta:
                while True:
                    self.mostrar_menu()
                    opcion = input("Seleccione una opción: ")

                    if opcion == "1":
                        cuenta.consultar_saldo()
                    elif opcion == "2":
                        monto = float(input("Ingrese el monto a depositar: "))
                        cuenta.depositar(monto)
                    elif opcion == "3":
                        monto = float(input("Ingrese el monto a retirar: "))
                        cuenta.retirar(monto)
                    elif opcion == "4":
                        numero_cuenta_destino = input("Ingrese el número de cuenta destino: ")
                        cuenta_destino = self.cuentas.get(numero_cuenta_destino)
                        if cuenta_destino:
                            monto = float(input("Ingrese el monto a transferir: "))
                            cuenta.transferir(monto, cuenta_destino)
                        else:
                            print("La cuenta destino no existe.")
                    elif opcion == "5":
                        cuenta.mostrar_historial()
                    elif opcion == "6":
                        print("Gracias por usar el cajero automático. ¡Hasta luego!")
                        break
                    else:
                        print("Opción no válida, por favor intente de nuevo.")
            else:
                print("Autenticación fallida. Inténtelo de nuevo.")

cajero = CajeroAutomatico()
cajero.agregar_cuenta("123456", "1111", 500)
cajero.agregar_cuenta("654321", "2222", 1000)

cajero.ejecutar()
