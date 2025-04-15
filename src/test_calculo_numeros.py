import unittest
from unittest.mock import patch
from calculo_numeros import ingrese_numero
from excepcion import NegativeNumberError

class TestIngresoNumero(unittest.TestCase):

   @patch('builtins.input', return_value='ABC')
    def test_entrada_no_numerica(self, mocked_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

if __name__ == '__main__':
    unittest.main()