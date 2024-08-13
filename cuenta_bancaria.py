class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre.capitalize()
        self.apellido = apellido.capitalize()


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"""
        Cliente: {self.nombre} {self.apellido}
        Numero de cuenta: {self.numero_cuenta}
        Saldo: {self.balance} €"""

    def depositar(self, importe):
        if importe > 0:
            self.balance += importe
            print(f"\n¡Depósito de {importe:.2f} € aceptado!")
        else:
            print("El importe debe ser un valor positivo.")

    def retirar(self, importe_retirar):
        if importe_retirar > 0:
            if self.balance >= importe_retirar:
                self.balance -= importe_retirar
                print(f"\n¡Retiro de {importe_retirar:.2f} € realizado!")
            else:
                print("\n¡Operación rechazada por saldo insuficiente!")
        else:
            print("\nEl importe debe ser un valor positivo.")

    def mostrar_info(self):
        print(self)


def crear_cliente():
    n = str(input("Nombre: ")).strip()
    a = str(input("Apellido: ")).strip()
    c = str(input("Numero de cuenta: ")).strip()

    while not c.isdigit():
        print("Número de cuenta inválido. Debe contener solo números.")
        c = input("Número de cuenta (solo números): ").strip()

    cliente = Cliente(n, a, c)
    return cliente


def inicio():
    mi_cliente = crear_cliente()

    while True:
        print("""
        ¡Hola! Elige una de las opciones: 
        [1] Depositar
        [2] Retirar
        [3] Mostrar información del cliente
        [4] Salir""")

        opcion = input("Opción: ").strip()

        if opcion == "1":
            try:
                valor_deposito = float(input("¿Cuánto quieres depositar? "))
                mi_cliente.depositar(valor_deposito)
            except ValueError:
                print("Por favor, ingresa un valor numérico válido.")

        elif opcion == "2":
            try:
                monto_retiro = float(input("Monto a retirar: "))
                mi_cliente.retirar(monto_retiro)
            except ValueError:
                print("Por favor, ingresa un valor numérico válido.")

        elif opcion == "3":
            mi_cliente.mostrar_info()

        elif opcion == "4":
            print("\nGracias por operar en Banco Python")
            break

        else:
            print("Opción no válida. Por favor, elige una opción válida.")


inicio()




