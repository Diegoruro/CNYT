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
        #primer_test
        resultado=complejos.resta([3,9],[1,5])
        self.assertEqual(resultado,[2,4])
        #segundo_test
        resultado=complejos.resta([2,9],[2,9])
        self.assertEqual(resultado,[0,0])
        #tercer_test
        resultado=complejos.resta([2.5,0],[4,1])
        self.assertEqual(resultado,[-1.5,-1])
        #cuarto_test
        resultado=complejos.resta([2/2,2],[1,12/3])
        self.assertEqual(resultado,[0,-2])

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
        resultado = complejos.division([20/10, 50/5], [10/5, 0.5])
        self.assertEqual(resultado, [2.118, 4.471])
    #todo terminar esto xdddd
if __name__ == '__main__':
    unittest.main()
