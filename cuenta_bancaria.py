class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


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
        self.balance += importe
        print("¡Depósito aceptado!")


    def retirar(self, importe_retirar):
        if self.balance < importe_retirar:
            print("¡Operación rechazada por saldo insuficiente!")
        else:
            self.balance -= importe_retirar
            print("¡Retiro realizado!")


def crear_cliente():
    n = str(input("Nombre: ")).capitalize()
    a = str(input("Apellido: ")).capitalize()
    c = str(input("Numero de cuenta: ")).strip()
    cliente = Cliente(n, a, c)
    return cliente


def inicio():
    mi_cliente = crear_cliente()
    opcion = " "
    while opcion != "3":
        print("""
            ¡Hola! Elige una de las opciones: 
            [1] Depositar
            [2] Retirar
            [3] Salir""")
        opcion = input()
        if opcion == "1":
            valor_deposito = int(input("Cuanto quieres depositar? "))
            mi_cliente.depositar(valor_deposito)
        elif opcion == '2':
            monto_ret = int(input("Monto a retirar: "))
            mi_cliente.retirar(monto_ret)
    print(mi_cliente)

    print("\nGracias por operar en Banco Python")


inicio()




