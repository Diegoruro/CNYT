import unittest
import complejos
from complejos import *


class Testcomplex(unittest.TestCase):
    def test_suma(self):
        # primer_test
        resultado = complejos.suma([1, 2], [3, 4])
        self.assertEqual(resultado, [4, 6])
        # segundo_test
        resultado = complejos.suma([10, 3], [2, 19])
        self.assertEqual(resultado, [12, 22])
        # tercer_test
        resultado = complejos.suma([2.5, 3], [1.5, 3.5])
        self.assertEqual(resultado, [4.0, 6.5])
        # cuarto_test
        resultado = complejos.suma([2 * 2, 4 * 3], [1 * 10, 3 * 3])
        self.assertEqual(resultado, [14, 21])

    def test_resta(self):
        # primer_test
        resultado = complejos.resta([3, 9], [1, 5])
        self.assertEqual(resultado, [2, 4])
        # segundo_test
        resultado = complejos.resta([2, 9], [2, 9])
        self.assertEqual(resultado, [0, 0])
        # tercer_test
        resultado = complejos.resta([2.5, 0], [4, 1])
        self.assertEqual(resultado, [-1.5, -1])
        # cuarto_test
        resultado = complejos.resta([2 / 2, 2], [1, 12 / 3])
        self.assertEqual(resultado, [0, -2])

    def test_multi(self):
        # primer_test
        resultado = complejos.multi([3, 9], [1, 5])
        self.assertEqual(resultado, [-42, 24])
        # segundo_test
        resultado = complejos.multi([1, 6], [6, 1])
        self.assertEqual(resultado, [0, 37])
        # tercer_test
        resultado = complejos.multi([0, 20], [4, 3])
        self.assertEqual(resultado, [-60, 80])
        # cuarto_test
        resultado = complejos.multi([4, 1.5], [0.5, 3])
        self.assertEqual(resultado, [-2.5, 12.75])

    def test_divi(self):
        # primer_test
        resultado = complejos.division([6, 5], [3, 2])
        self.assertEqual(resultado, [2.154, 0.231])
        # segundo_test
        resultado = complejos.division([6, 5], [5, 6])
        self.assertEqual(resultado, [0.984, -0.180])
        # tercer_test
        resultado = complejos.division([5, 20], [10, 2])
        self.assertEqual(resultado, [0.865, 1.827])
        # cuarto_test
        resultado = complejos.division([20 / 10, 50 / 5], [10 / 5, 0.5])
        self.assertEqual(resultado, [2.118, 4.471])

    def test_modulo(self):
        # primer_test
        resultado = complejos.modulo([1, 1])
        self.assertEqual(resultado, 1.414)
        # segundo_test
        resultado = complejos.modulo([3, 4])
        self.assertEqual(resultado, 5)
        # tercer_test
        resultado = complejos.modulo([1 + 2, 4 + 3])
        self.assertEqual(resultado, 7.616)
        # cuarto_test
        resultado = complejos.modulo([0.5, 1.5])
        self.assertEqual(resultado, 1.581)

    def test_conjugado(self):
        # primer_test
        resultado = complejos.conjugado([1, 1])
        self.assertEqual(resultado, [1, -1])
        # segundo_test
        resultado = complejos.conjugado([1, -6])
        self.assertEqual(resultado, [1, 6])
        # tercer_test
        resultado = complejos.conjugado([1, -1.5])
        self.assertEqual(resultado, [1, 1.5])
        # cuarto_test
        resultado = complejos.conjugado([1, 20 / 2])
        self.assertEqual(resultado, [1, -10])

    def test_polares(self):
        # primer_test
        resultado = complejos.polares([1, 1])
        self.assertEqual(resultado, [1.414, 0.785])
        # segundo_test
        resultado = complejos.polares([3, 4])
        self.assertEqual(resultado, [5, 0.927])
        # tercer_test
        resultado = complejos.polares([4, 3])
        self.assertEqual(resultado, [5, 0.644])
        # cuarto_test
        resultado = complejos.polares([1, 0])
        self.assertEqual(resultado, [1, 0])

    def test_cartesianos(self):
        # primer_test
        resultado = complejos.cartesianos([1, 0])
        self.assertEqual(resultado, [1, 0])
        # segundo_test
        resultado = complejos.cartesianos([0, 45])
        self.assertEqual(resultado, [0, 0])
        # tercer_test
        resultado = complejos.cartesianos([2, 0.524])
        self.assertEqual(resultado, [1.732, 1.001])
        # cuarto_test
        resultado = complejos.cartesianos([1.414, 0.785])
        self.assertEqual(resultado, [1.0, 0.999])

    def test_fase(self):
        # primer_test
        resultado = complejos.fase([1, 0])
        self.assertEqual(resultado, 0)
        # segundo_test
        resultado = complejos.fase([1, 1])
        self.assertEqual(resultado, 0.785)
        # tercer_test
        resultado = complejos.fase([1.732, 1])
        self.assertEqual(resultado, 0.524)
        # cuarto_test
        resultado = complejos.fase([1, 1.732])
        self.assertEqual(resultado, 1.047)


if __name__ == '__main__':
    unittest.main()

