import unittest
import new_complejos
from new_complejos import *


class Testcomplex(unittest.TestCase):
    def test_suma(self):
        # primer_test
        resultado = new_complejos.suma([1, 2], [3, 4])
        self.assertEqual(resultado, (4, 6))
        # segundo_test
        resultado = new_complejos.suma([10, 3], [2, 19])
        self.assertEqual(resultado, (12, 22))
        # tercer_test
        resultado = new_complejos.suma([2.5, 3], [1.5, 3.5])
        self.assertEqual(resultado, (4.0, 6.5))
        # cuarto_test
        resultado = new_complejos.suma([2 * 2, 4 * 3], [1 * 10, 3 * 3])
        self.assertEqual(resultado, (14, 21))

    def test_resta(self):
        # primer_test
        resultado = new_complejos.resta([3, 9], [1, 5])
        self.assertEqual(resultado, (2, 4))
        # segundo_test
        resultado = new_complejos.resta([2, 9], [2, 9])
        self.assertEqual(resultado, (0, 0))
        # tercer_test
        resultado = new_complejos.resta([2.5, 0], [4, 1])
        self.assertEqual(resultado, (-1.5, -1))
        # cuarto_test
        resultado = new_complejos.resta([2 / 2, 2], [1, 12 / 3])
        self.assertEqual(resultado, (0, -2))

    def test_multi(self):
        # primer_test
        resultado = new_complejos.multi([3, 9], [1, 5])
        self.assertEqual(resultado, (-42, 24))
        # segundo_test
        resultado = new_complejos.multi([1, 6], [6, 1])
        self.assertEqual(resultado, (0, 37))
        # tercer_test
        resultado = new_complejos.multi([0, 20], [4, 3])
        self.assertEqual(resultado, (-60, 80))
        # cuarto_test
        resultado = new_complejos.multi([4, 1.5], [0.5, 3])
        self.assertEqual(resultado, (-2.5, 12.75))

    def test_divi(self):
        # primer_test
        resultado = new_complejos.division([6, 5], [3, 2])
        self.assertEqual(resultado, (2.154, 0.231))
        # segundo_test
        resultado = new_complejos.division([6, 5], [5, 6])
        self.assertEqual(resultado, (0.984, -0.180))
        # tercer_test
        resultado = new_complejos.division([5, 20], [10, 2])
        self.assertEqual(resultado, (0.865, 1.827))
        # cuarto_test
        resultado = new_complejos.division([20 / 10, 50 / 5], [10 / 5, 0.5])
        self.assertEqual(resultado, (2.118, 4.471))

    def test_modulo(self):
        # primer_test
        resultado = new_complejos.modulo([1, 1])
        self.assertEqual(resultado, 1.41)
        # segundo_test
        resultado = new_complejos.modulo([3, 4])
        self.assertEqual(resultado, 5)
        # tercer_test
        resultado = new_complejos.modulo([1 + 2, 4 + 3])
        self.assertEqual(resultado, 7.62)
        # cuarto_test
        resultado = new_complejos.modulo([0.5, 1.5])
        self.assertEqual(resultado, 1.58)

    def test_conjugado(self):
        # primer_test
        resultado = new_complejos.conjugado([1, 1])
        self.assertEqual(resultado, (1, -1))
        # segundo_test
        resultado = new_complejos.conjugado([1, -6])
        self.assertEqual(resultado, (1, 6))
        # tercer_test
        resultado = new_complejos.conjugado([1, -1.5])
        self.assertEqual(resultado, (1, 1.5))
        # cuarto_test
        resultado = new_complejos.conjugado([1, 20 / 2])
        self.assertEqual(resultado, (1, -10))

    def test_polares(self):
        # primer_test
        resultado = new_complejos.polares([1, 1])
        self.assertEqual(resultado, (1.41, 0.785))
        # segundo_test
        resultado = new_complejos.polares([3, 4])
        self.assertEqual(resultado, (5, 0.927))
        # tercer_test
        resultado = new_complejos.polares([4, 3])
        self.assertEqual(resultado, (5, 0.644))
        # cuarto_test
        resultado = new_complejos.polares([1, 0])
        self.assertEqual(resultado, (1, 0))

    def test_cartesianos(self):
        # primer_test
        resultado = new_complejos.cartesianos([1, 0])
        self.assertEqual(resultado, (1, 0))
        # segundo_test
        resultado = new_complejos.cartesianos([0, 45])
        self.assertEqual(resultado, (0, 0))
        # tercer_test
        resultado = new_complejos.cartesianos([2, 0.524])
        self.assertEqual(resultado, (1.732, 1.001))
        # cuarto_test
        resultado = new_complejos.cartesianos([1.414, 0.785])
        self.assertEqual(resultado, (1.0, 0.999))

    def test_fase(self):
        # primer_test
        resultado = new_complejos.fase([1, 0])
        self.assertEqual(resultado, 0)
        # segundo_test
        resultado = new_complejos.fase([1, -1])
        self.assertEqual(resultado, 7.068)
        # tercer_test
        resultado = new_complejos.fase([-1.732, -1])
        self.assertEqual(resultado, 3.666)
        # cuarto_test
        resultado = new_complejos.fase([-1, 1.732])
        self.assertEqual(resultado, 4.189)

    def test_suma_vecto(self):
        # primer_test
        resultado = new_complejos.suma_vecto([[1, 0], [2, 0]], [[1, 2], [3, 4]])
        self.assertEqual(resultado, [(2, 2), (5, 4)])
        # segundo_test
        resultado = new_complejos.suma_vecto([[10, 0], [2, 0]], [[-10, 2], [-4, 4]])
        self.assertEqual(resultado, [(0, 2), (-2, 4)])
        # tercer_test
        resultado = new_complejos.suma_vecto([[5 + 5, 0], [2, 5]], [[-15, 3], [3, -5]])
        self.assertEqual(resultado, [(-5, 3), (5, 0)])
        # cuarto_test
        resultado = new_complejos.suma_vecto([[1, 0], [2, 0]], [[1, 2], [3, 4]])
        self.assertEqual(resultado, [(2, 2), (5, 4)])

    def test_inverse_vecto(self):
        # primer_test
        resultado = new_complejos.inverse_vecto([[1, 0], [2, 0]])
        self.assertEqual(resultado, [(-1, 0), (-2, 0)])
        # segunda_test
        resultado = new_complejos.inverse_vecto([[1, -5], [2, -7]])
        self.assertEqual(resultado, [(-1, 5), (-2, 7)])
        # tercer_test
        resultado = new_complejos.inverse_vecto([[1, 7], [2, -56]])
        self.assertEqual(resultado, [(-1, -7), (-2, 56)])
        # cuarto_test
        resultado = new_complejos.inverse_vecto([[-4, 0], [2, 0]])
        self.assertEqual(resultado, [(4, 0), (-2, 0)])

    def test_multi_esc(self):
        # primer_test
        resultado = new_complejos.multi_esc((1, 0), [(2, 0), (5, 4)])
        self.assertEqual(resultado, [(2, 0), (5, 4)])
        # segundo_test
        resultado = new_complejos.multi_esc((5, 1), [(3, 2), (5, 4)])
        self.assertEqual(resultado, [(13, 13), (21, 25)])
        # tercer_test
        resultado = new_complejos.multi_esc((0, 0), [(3, 2), (5, 4)])
        self.assertEqual(resultado, [(0, 0), (0, 0)])
        # cuarto_test
        resultado = new_complejos.multi_esc((3, 6), [(10, 7), (7, 3)])
        self.assertEqual(resultado, [(-12, 81), (3, 51)])

    def test_suma_mat(self):
        # primer_test
        resultado = new_complejos.suma_mat([[(1, 0), (2, 0)], [(3, 4), (4, 5)]], [[(4, 5), (1, 3)], [(6, 7), (8, 9)]])
        self.assertEqual(resultado, [[(5, 5), (3, 3)], [(9, 11), (12, 14)]])
        # segundo_test
        resultado = new_complejos.suma_mat([[(1, 0), (2, 0)], [(3, 4), (4, 5)], [(1, 4), (3, 2)]],
                                           [[(4, 5), (1, 3)], [(1, 4), (3, 2)], [(4, 4), (4, 5)]])
        self.assertEqual(resultado, [[(5, 5), (3, 3)], [(4, 8), (7, 7)], [(5, 8), (7, 7)]])
        # tercer_test
        resultado = new_complejos.suma_mat([[(1, 1), (2, -3)], [(3, -4), (4, -5)]],
                                           [[(-4, 5), (1, 3)], [(6, -7), (-8, 9)]])
        self.assertEqual(resultado, [[(-3, 6), (3, 0)], [(9, -11), (-4, 4)]])
        # cuarto_test
        resultado = new_complejos.suma_mat([[(1, -5), (2, 5)], [(3, -4), (-4, 5)], [(1, -4), (3, -2)]],
                                           [[(4, 5), (1, -3)], [(1, -4), (3, 2)], [(-4, 4), (4, 5)]])
        self.assertEqual(resultado, [[(5, 0), (3, 2)], [(4, -8), (-1, 7)], [(-3, 0), (7, 3)]])

    def test_inverse_mat(self):
        # primer_test
        resultado = new_complejos.inverse_mat([[(1, -5), (2, 5)], [(3, -4), (-4, 5)], [(1, -4), (3, -2)]])
        self.assertEqual(resultado, [[(-1, 5), (-2, -5)], [(-3, 4), (4, -5)], [(-1, 4), (-3, 2)]])
        # segundo_test
        resultado = new_complejos.inverse_mat([[(1, 0), (2, 0)], [(3, 4), (4, 5)], [(1, 4), (3, 2)]])
        self.assertEqual(resultado, [[(-1, 0), (-2, 0)], [(-3, -4), (-4, -5)], [(-1, -4), (-3, -2)]])
        # tercer_test
        resultado = new_complejos.inverse_mat([[(4, 5), (1, -3)], [(1, -4), (3, 2)], [(-4, 4), (4, 5)]])
        self.assertEqual(resultado, [[(-4, -5), (-1, 3)], [(-1, 4), (-3, -2)], [(4, -4), (-4, -5)]])
        # cuarto_test
        resultado = new_complejos.inverse_mat([[(1, 1), (2, -3)], [(3, -4), (4, -5)]])
        self.assertEqual(resultado, [[(-1, -1), (-2, 3)], [(-3, 4), (-4, 5)]])

    def test_multi_esc_mat(self):
        # primer_test
        resultado = new_complejos.multi_esc_mat((1, 0), [[(1, 0), (2, 0)], [(3, 4), (4, 5)], [(1, 4), (3, 2)]])
        self.assertEqual(resultado, [[(1, 0), (2, 0)], [(3, 4), (4, 5)], [(1, 4), (3, 2)]])
        # segundo_test
        resultado = new_complejos.multi_esc_mat((-4, 2), [[(4, 5), (1, 3)], [(1, 4), (3, 2)], [(4, 4), (4, 5)]])
        self.assertEqual(resultado, [[(-26, -12), (-10, -10)], [(-12, -14), (-16, -2)], [(-24, -8), (-26, -12)]])
        # tercer_test
        resultado = new_complejos.multi_esc_mat((2, 3), [[(2, 0), (5, 4)], [(4, 5), (3, 5)]])
        self.assertEqual(resultado, [[(4, 6), (-2, 23)], [(-7, 22), (-9, 19)]])
        # cuarto_test
        resultado = new_complejos.multi_esc_mat((-2, 10), [[(1, -5), (2, 5)], [(3, -4), (-4, 5)], [(1, -4), (3, -2)]])
        self.assertEqual(resultado, [[(48, 20), (-54, 10)], [(34, 38), (-42, -50)], [(38, 18), (14, 34)]])

    def test_traspuesta(self):
        # primer_test
        resultado = new_complejos.traspuesta([[(1, 0), (2, 0)]])
        self.assertEqual(resultado, [[(1, 0)], [(2, 0)]])
        # segundo_test
        resultado = new_complejos.traspuesta([[(4, 5), (4, 3)]])
        self.assertEqual(resultado, [[(4, 5)], [(4, 3)]])
        # tercer_test
        resultado = new_complejos.traspuesta([[(48, 20), (-54, 10)], [(34, 38), (-42, -50)], [(38, 18), (14, 34)]])
        self.assertEqual(resultado, [[(48, 20), (34, 38), (38, 18)], [(-54, 10), (-42, -50), (14, 34)]])
        # cuarto_test
        resultado = new_complejos.traspuesta([[(1, -5), (2, 5)], [(3, -4), (-4, 5)], [(1, -4), (3, -2)]])
        self.assertEqual(resultado, [[(1, -5), (3, -4), (1, -4)], [(2, 5), (-4, 5), (3, -2)]])

    def test_conjugada_mat(self):
        # primer_test
        resultado = new_complejos.conjugada_mat([[(1, 0), (2, 0)], [(3, 4), (4, 3)]])
        self.assertEqual(resultado, [[(1, 0), (2, 0)], [(3, -4), (4, -3)]])
        # segundo_test
        resultado = new_complejos.conjugada_mat([[(1, -5), (2, 5)], [(3, -4), (-4, 5)], [(1, -4), (3, -2)]])
        self.assertEqual(resultado, [[(1, 5), (2, -5)], [(3, 4), (-4, -5)], [(1, 4), (3, 2)]])
        # tercer_test
        resultado = new_complejos.conjugada_mat([[(2, 0), (5, 4)], [(4, 5), (3, 5)]])
        self.assertEqual(resultado, [[(2, 0), (5, -4)], [(4, -5), (3, -5)]])
        # cuarto_test
        resultado = new_complejos.conjugada_mat([[(48, 20), (-54, 10)], [(34, 38), (-42, -50)], [(38, 18), (14, 34)]])
        self.assertEqual(resultado, [[(48, -20), (-54, -10)], [(34, -38), (-42, 50)], [(38, -18), (14, -34)]])

    def test_adjunta(self):
        # primer_test
        resultado = new_complejos.adjunta([[(48, 20), (-54, 10)], [(34, 38), (-42, -50)], [(38, 18), (14, 34)]])
        self.assertEqual(resultado, [[(48, -20), (34, -38), (38, -18)], [(-54, -10), (-42, 50), (14, -34)]])
        # segundo_test
        resultado = new_complejos.adjunta([[(1, -5), (2, 5)], [(3, -4), (-4, 5)], [(1, -4), (3, -2)]])
        self.assertEqual(resultado, [[(1, 5), (3, 4), (1, 4)], [(2, -5), (-4, -5), (3, 2)]])
        # tercer_test
        resultado = new_complejos.adjunta([[(1, 0), (2, 0)]])
        self.assertEqual(resultado, [[(1, 0)], [(2, 0)]])
        # cuarto_test
        resultado = new_complejos.adjunta([[(4, 5), (4, 3)]])
        self.assertEqual(resultado, [[(4, -5)], [(4, -3)]])

    def test_producto(self):
        # primer_test
        resultado = new_complejos.producto([[(1, 0), (2, 0)], [(3, 4), (4, 5)]], [[(4, 5), (1, 3)], [(6, 7), (8, 9)]])
        self.assertEqual(resultado, [[(16, 19), (17, 21)], [(-19, 89), (-22, 89)]])
        # segundo_test
        resultado = new_complejos.producto([[(1, 0), (2, 0), (3, 5)], [(3, 4), (4, 5), (6, 9)]],
                                           [[(4, 5), (1, 3)], [(6, 7), (8, 9)]])
        self.assertEqual(resultado, "Is not possible")
        # tercer_test
        resultado = new_complejos.producto([[(1, 0), (0, 0)], [(0, 0), (1, 0)]], [[(4, 5), (1, 3)], [(6, 7), (8, 9)]])
        self.assertEqual(resultado, [[(4, 5), (1, 3)], [(6, 7), (8, 9)]])
        # cuarto_test
        resultado = new_complejos.producto([[(1, 0), (0, 0)], [(0, 0), (1, 0)]], [[(6, 7), (8, 9)]])
        self.assertEqual(resultado, "Is not possible")

    def test_accion(self):
        # primer_test
        resultado = new_complejos.Accion([[(1, 0), (2, 0)], [(3, 4), (4, 5)]], [[(4, 5)], [(1, 3)]])
        self.assertEqual(resultado, [[(6, 11)], [(-19, 48)]])
        # segundo_test
        resultado = new_complejos.Accion([[(1, 0), (2, 0)], [(3, 4), (4, 5)]], [[(4, 5), (1, 3)]])
        self.assertEqual(resultado, "Is not possible")
        # tercer_test
        resultado = new_complejos.Accion([[(1, 0), (2, 0), (6, 45)], [(3, 4), (4, 5), (4, 6)], ],
                                         [[(4, 5)], [(1, 3)], [(29, 54)]])
        self.assertEqual(resultado, [[(-2250, 1640)], [(-227, 438)]])
        # cuarto_test
        resultado = new_complejos.Accion([[(1, 0), (2, 0), (6, 45), (4, 6)], [(3, 4), (4, 5), (4, 6), (3, 7)], ],
                                         [[(4, 5)], [(1, 3)], [(29, 54)], [(31, 66)]])
        self.assertEqual(resultado, [[(-2522, 2090)], [(-596, 853)]])

    def test_producto_interno(self):
        # primer_test
        resultado = new_complejos.product_int([(3, 1), (2, 6), (7, 5), (3, 6)], [(4, 5), (1, 3), (29, 54), (31, 66)])
        self.assertEqual(resultado, (-379, 938))
        # segundo_test
        resultado = new_complejos.product_int([(1, 0), (1, 0), (0, 1), (0, 1)], [(4, 5), (1, 3), (29, 54), (31, 66)])
        self.assertEqual(resultado, (-115, 68))
        # tercer_test
        resultado = new_complejos.product_int([(0, 0), (0, 0), (0, 0), (0, 0)], [(4, 5), (1, 3), (29, 54), (31, 66)])
        self.assertEqual(resultado, (0, 0))
        # cuarto_test
        resultado = new_complejos.product_int([(4, 2), (2, 6), (6, 3), (7, 8)], [(5, 1), (4, 2), (6, 3), (1, 7)])
        self.assertEqual(resultado, (-8, 135))

    def test_norma(self):
        # primer_test
        resultado = new_complejos.norma([(4, 2), (2, 6), (6, 3), (7, 8)])
        self.assertEqual(resultado, 14.76)
        # segundo_test
        resultado = new_complejos.norma([(5, 1), (4, 2), (6, 3), (1, 7)])
        self.assertEqual(resultado, 11.87)
        # tercer_test
        resultado = new_complejos.norma([(4, 5), (1, 3), (29, 54), (31, 66)])
        self.assertEqual(resultado, 95.52)
        # cuarto_test
        resultado = new_complejos.norma([[1, 0], [2, 0]])
        self.assertEqual(resultado, 2.24)

    def test_distancia(self):
        # primer_test
        resultado = new_complejos.distancia([(5, 1), (4, 2), (6, 3), (1, 7)], [(3, 1), (2, 6), (7, 5), (3, 6)])
        self.assertEqual(resultado, 5.83)
        # segundo_test
        resultado = new_complejos.distancia([(1, 0), (2, 0)], [(3, 4), (4, 5)])
        self.assertEqual(resultado, 7.0)
        # tercer_test
        resultado = new_complejos.distancia([(4, 5), (1, 3)], [(3, 4), (4, 5)])
        self.assertEqual(resultado, 3.88)
        # cuarto_test
        resultado = new_complejos.distancia([(7, 3), (3, 5), (7, 4), (8, 5)], [(1, 2), (7, 3), (7, 8), (2, 4)])
        self.assertEqual(resultado, 10.48)

    def test_unit(self):
        # primer_test
        resultado = new_complejos.unit([[(2 / 3, 0.0), (-2 / 3, 1 / 3)], [(2 / 3, 1 / 3), (2 / 3, 0.0)]])
        self.assertEqual(resultado, True)
        # primer_test
        resultado = new_complejos.unit([[(0, 0), (0, 1)], [(0, 1), (0, 0)]])
        self.assertEqual(resultado, True)
        # primer_test
        resultado = new_complejos.unit([[(0, 2), (0, 1)], [(0, 4), (2, 0)]])
        self.assertEqual(resultado, False)
        # primer_test
        resultado = new_complejos.unit([[(1, 0), (2, 0)], [(0, 4), (2, 0)], [(0, 4), (2, 0)]])
        self.assertEqual(resultado, "The input have to be a square matrix")

    def test_herm(self):
        # primer_test
        resultado = new_complejos.herm([[(7, 0), (6, 5)], [(6, -5), (-3, 0)]])
        self.assertEqual(resultado, True)
        # segundo_test
        resultado = new_complejos.herm([[(5, 1), (4, 2)], [(6, 3), (1, 7)]])
        self.assertEqual(resultado, False)
        # tercer_test
        resultado = new_complejos.herm([[(5, 0), (3, 7)], [(3, -7), (2, 0)]])
        self.assertEqual(resultado, True)
        # cuarto_test
        resultado = new_complejos.herm([[(1, 0), (2, 4)], [(2, -4), (3, 0)]])
        self.assertEqual(resultado, True)

    def test_tensor(self):
        # primer_test
        resultado = new_complejos.tensor([[(3, 2), (5, -1), (0, 2)], [(0, 0), (12, 0), (6, -3)], [(2, 0), (4, 4), (9, 3)]], [[(1, 0), (3, 4), (5, -7)], [(10, 2), (6, 0), (2, 5)], [(0, 0), (1, 0), (2, 9)]])
        self.assertEqual(resultado, [[[[(3, 2), (1, 18), (29, -11)], [(26, 26), (18, 12), (-4, 19)], [(0, 0), (3, 2), (-12, 31)]], [[(5, -1), (19, 17), (18, -40)], [(52, 0), (30, -6), (15, 23)], [(0, 0), (5, -1), (19, 43)]], [[(0, 2), (-8, 6), (14, 10)], [(-4, 20), (0, 12), (-10, 4)], [(0, 0), (0, 2), (-18, 4)]]], [[[(0, 0), (0, 0), (0, 0)], [(0, 0), (0, 0), (0, 0)], [(0, 0), (0, 0), (0, 0)]], [[(12, 0), (36, 48), (60, -84)], [(120, 24), (72, 0), (24, 60)], [(0, 0), (12, 0), (24, 108)]], [[(6, -3), (30, 15), (9, -57)], [(66, -18), (36, -18), (27, 24)], [(0, 0), (6, -3), (39, 48)]]], [[[(2, 0), (6, 8), (10, -14)], [(20, 4), (12, 0), (4, 10)], [(0, 0), (2, 0), (4, 18)]], [[(4, 4), (-4, 28), (48, -8)], [(32, 48), (24, 24), (-12, 28)], [(0, 0), (4, 4), (-28, 44)]], [[(9, 3), (15, 45), (66, -48)], [(84, 48), (54, 18), (3, 51)], [(0, 0), (9, 3), (-9, 87)]]]]
)

if __name__ == '__main__':
    unittest.main()
