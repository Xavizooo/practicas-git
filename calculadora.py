class Calculadora:
    def __init__(self, a: float, b:float):
        self.a = a
        self.b = b
    def sumar(self):
        return self.a + self.b
    def restar(self):
        return self.a - self.b
    def dividir(self):
        if self.b == 0:
            return "No se puede dividir por 0"
        else:
            return self.a / self.b
        