import unittest
import ClassicToQuantum
from ClassicToQuantum import *


class Testcomplex(unittest.TestCase):
    def test_experimentbool(self):
        # primer_test
        resultado = ClassicToQuantum.experimentBool(
            [[False, False, False, False, False, False], [True, False, False, False, False, True],
             [False, True, False, False, False, False], [False, False, True, False, False, False],
             [False, False, False, True, False, False], [False, False, False, False, True, False]],
            [True, False, False, False, True, False], 3)
        self.assertEqual(resultado, [False, False, True, True, False, False])
        # segundo_test
        resultado = ClassicToQuantum.experimentBool(
            [[False, False, False, False, False, False], [True, False, False, False, False, True],
             [False, True, False, False, False, False], [False, False, True, False, False, False],
             [False, False, False, True, False, False], [False, False, False, False, True, False]],
            [True, False, False, False, True, False], 1)
        self.assertEqual(resultado, [False, True, False, False, False, True])
        # tercer_test
        resultado = ClassicToQuantum.experimentBool(
            [[False, False, False, False, False, False], [True, False, False, False, False, True],
             [False, True, False, False, False, False], [False, False, True, False, False, False],
             [False, False, False, True, False, False], [False, False, False, False, True, False]],
            [True, False, False, False, True, False], 5)
        self.assertEqual(resultado, [False, False, False, False, True, True])
        # cuarto_test
        resultado = ClassicToQuantum.experimentBool(
            [[False, False, False, False, False, False], [True, False, False, False, False, True],
             [False, True, False, False, False, False], [False, False, True, False, False, False],
             [False, False, False, True, False, False], [False, False, False, False, True, False]],
            [True, False, False, False, True, False, False], 5)
        self.assertEqual(resultado, "Length error")

    def test_matriz_reales(self):
        # primer_test
        resultado = ClassicToQuantum.matriz_reales([[0, 1 / 6, 5 / 6], [1 / 3, 1 / 2, 1 / 6], [2 / 3, 1 / 3, 0]],
                                                   [1 / 5, 7 / 10, 1 / 10], 1)
        self.assertEqual(resultado, [0.2, 0.4333333333333333, 0.36666666666666664])
        # segundo_test
        resultado = ClassicToQuantum.matriz_reales([[0, 1 / 6, 5 / 6], [1 / 3, 1 / 2, 1 / 6], [2 / 3, 1 / 3, 0]],
                                                   [1 / 5, 7 / 10, 1 / 10], 3)
        self.assertEqual(resultado, [0.2888888888888889, 0.34444444444444444, 0.36666666666666664])
        # tercer_test
        resultado = ClassicToQuantum.matriz_reales([[0, 1 / 6, 5 / 6], [1 / 3, 1 / 2, 1 / 6], [2 / 3, 1 / 3, 0]],
                                                   [1 / 5, 7 / 10, 1 / 10], 5)
        self.assertEqual(resultado, [0.3111111111111111, 0.337037037037037, 0.3518518518518518])
        # tercer_test
        resultado = ClassicToQuantum.matriz_reales([[0, 1 / 6, 5 / 6], [1 / 3, 1 / 2, 1 / 6], [2 / 3, 1 / 3, 0]],
                                                   [1 / 5, 7 / 10, 1 / 10, 3], 5)
        self.assertEqual(resultado, "Length error")

    def test_matriz_complex(self):
        # primer_test
        resultado = ClassicToQuantum.matriz_complex(
            [[(1 / (2 ** 0.5), 0), (0, 1 / (2 ** 0.5))], [(1 / (2 ** 0.5), 0), (0, -1 / (2 ** 0.5))]], [(1, 0), (0, 0)],
            1)
        self.assertEqual(resultado, [0.5041, 0.5041])
        # segundo_test
        resultado = ClassicToQuantum.matriz_complex(
            [[(1 / (2 ** 0.5), 0), (0, 1 / (2 ** 0.5))], [(1 / (2 ** 0.5), 0), (0, -1 / (2 ** 0.5))]], [(1, 0), (0, 0)],
            3)
        self.assertEqual(resultado, [1.0, 0.0])
        # tercer_test
        resultado = ClassicToQuantum.matriz_complex(
            [[(1 / (2 ** 0.5), 0), (0, 1 / (2 ** 0.5))], [(1 / (2 ** 0.5), 0), (0, -1 / (2 ** 0.5))]], [(1, 0), (0, 0)],
            5)
        self.assertEqual(resultado, [0.5041, 0.5041])
        # cuarto_test
        resultado = ClassicToQuantum.matriz_complex(
            [[(1 / (2 ** 0.5), 0), (0, 1 / (2 ** 0.5))], [(1 / (2 ** 0.5), 0), (0, -1 / (2 ** 0.5))]],
            [(1, 0), (0, 0), (0, 1)], 5)
        self.assertEqual(resultado, "Length error")
    def test_grafica(self):
        # primer_test
        resultado = ClassicToQuantum.grafica(
            [[(1 / (2 ** 0.5), 0), (0, 1 / (2 ** 0.5))], [(1 / (2 ** 0.5), 0), (0, -1 / (2 ** 0.5))]], [(1, 0), (0, 0)],
            1)

if __name__ == '__main__':
    unittest.main()
