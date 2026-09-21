import pytest
from calculadora import Calculadora

def test_sumar():
    calc = Calculadora(2, 3)
    assert calc.sumar() == 5
def test_sumar_negativos():
    calc = Calculadora(-2, -3)
    assert calc.sumar() == -5
def test_restar():
    calc = Calculadora(5, 3)
    assert calc.restar() == 2
def test_dividir():
    calc = Calculadora(12, 3)
    assert calc.dividir() == 4
def test_dividir_por_cero():
    calc = Calculadora(10, 0)
    assert calc.dividir() == "No se puede dividir por 0"