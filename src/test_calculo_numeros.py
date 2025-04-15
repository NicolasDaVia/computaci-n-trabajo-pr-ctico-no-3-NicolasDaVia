import unittest
from unittest.mock import patch
from calculo_numeros import ingrese_numero
from excepcion import NegativeNumberError

class TestIngresoNumero(unittest.TestCase):


     @patch('builtins.input', return_value='-50')
    def test_numero_negativo(self, mocked_input):
        with self.assertRaises(NegativeNumberError):
            ingrese_numero()

if __name__ == '__main__':
    unittest.main()