
#Atributos privados en Python
print("Atributos privados en Python:")
class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    def mostrar_saldo(self):
        print("El saldo actual es:", self.__saldo)

    def depositar(self, cantidad):
        self.__saldo += cantidad
        print("Depósito realizado.")

cuenta = CuentaBancaria(1000)

cuenta.mostrar_saldo()
cuenta.depositar(500)
cuenta.mostrar_saldo()




#Crear varios objetos a partir de una misma clase
print("Crear varios objetos a partir de una misma clase:")
cuenta1 = CuentaBancaria(1000)
cuenta2 = CuentaBancaria(500)

print(cuenta1.mostrar_saldo())
print(cuenta2.mostrar_saldo())