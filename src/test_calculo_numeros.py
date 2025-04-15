import unittest
from unittest.mock import patch
from calculo_numeros import ingrese_numero
from excepcion import NegativeNumberError

class TestIngresoNumero(unittest.TestCase):

    @patch('builtins.input', return_value='100')
    def test_numero_valido(self, mocked_input):
        resultado = ingrese_numero()
        self.assertEqual(resultado, 100.0)
### 