class Calculadora:
    def __init__(self, numero1: float, numero2: float):
        self.numero1 = numero1
        self.numero2 = numero2
    def sumar(self):
        return self.numero1 + self.numero2
    def restar(self):
        return self.numero1 - self.numero2
    def multiplicar(self):
        return self.numero1 * self.numero2
    def dividir(self):
        if self.numero2 == 0:
            return "No se puede dividir por 0"
        else:
            return self.numero1 / self.numero2

entrada1 = float(input("Primero numero: "))
entrada2 = float(input("Segundp numero: "))
numero1 = entrada1
numero2 = entrada2

numeros = Calculadora(numero1, numero2)

print(numeros.dividir())