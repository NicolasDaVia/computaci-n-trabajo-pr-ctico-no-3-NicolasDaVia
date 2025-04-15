import unittest
from unittest.mock import patch
from calculo_numeros import ingrese_numero
from excepcion import NegativeNumberError

class TestIngresoNumero(unittest.TestCase):

    @patch('builtins.input', return_value='100')
    def test_numero_valido(self, mocked_input):
        resultado = ingrese_numero()
        self.assertEqual(resultado, 100.0)

    @patch('builtins.input', return_value='-50')
    def test_numero_negativo(self, mocked_input):
        with self.assertRaises(NegativeNumberError):
            ingrese_numero()

    @patch('builtins.input', return_value='ABC')
    def test_entrada_no_numerica(self, mocked_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

if __name__ == '__main__':
    unittest.main()

