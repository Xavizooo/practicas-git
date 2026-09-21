class Calculadora:
    """Realiza operaciones aritmeticas basicas entre dos numeros"""
    def __init__(self, a: float, b:float):
        """ Inicializa la calculadora con los dos operandos
        
        Args:
            a: primer numero
            b: segundo numero
        """
        self.a = a
        self.b = b
    def sumar(self):
        """
        Devuelve la suma entre a y b 
        """

        return self.a + self.b
    def restar(self):
        """
        Devuelve la resta entre a menos b
        """
        return self.a - self.b
    def dividir(self):
        """
        Divide entre b

        devuelve a / b o el texto "No se puede dividir por 0"
        """
        if self.b == 0:
            return "No se puede dividir por 0"
        else:
            return self.a / self.b
        