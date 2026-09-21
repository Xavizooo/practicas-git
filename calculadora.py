class Calculadora:
    def __init__(self, a: float, b:float):
        self.a = a
        self.b = b
    def sumar(self):
        return self.a + self.b
    def restar(self):
        return self.a - self.b
    def dividir(self):
        return self.a / self.b