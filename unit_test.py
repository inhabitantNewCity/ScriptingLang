import unittest
from polynomial import Polynomial


class TestPolynomial(unittest.TestCase):

    def test_init_correct_args(self):
        p = Polynomial([1, -1])
        self.assertEqual(p.coeffs, [1, -1])
        self.assertEqual(p.degree, 1)

    def test_init_infs_args(self):
        p = Polynomial([float("inf"), float("-inf")])
        self.assertEqual(p.coeffs, [float("inf"), float("-inf")])
        self.assertEqual(p.degree, 1)

    def test_init_empty_list(self):
        self.assertRaises(TypeError, Polynomial, [])

    def test_init_no_list(self):
        self.assertRaises(TypeError, Polynomial, "1")

    def test_init_zero_values_list(self):
        p = Polynomial([0, 0, 0])
        self.assertEqual(p.coeffs, [0])
        self.assertEqual(p.degree, 0)

    def test_eq_true(self):
        p1 = Polynomial([1, -1])
        p2 = Polynomial([1, -1])
        self.assertTrue(p1 == p2)


    def test_eq_inf_true(self):
        p1 = Polynomial([float("inf"), float("-inf")])
        p2 = Polynomial([float("inf"), float("-inf")])
        self.assertTrue(p1 == p2)

    def test_eq_false(self):
        p1 = Polynomial([1, -1])
        p2 = Polynomial([1, 1])
        self.assertFalse(p1 == p2)


    def test_eq_big_self_other_is_not_polynomial(self):
        p1 = Polynomial([1, -1])
        p2 = 1
        self.assertFalse(p1 == p2)

    def test_eq_other_is_string(self):
        p1 = Polynomial([2, 0, 0])
        self.assertRaises(TypeError, p1.__eq__, "2")

    def test_add_same_polyn_size(self):
        p1 = Polynomial([1, -1])
        p2 = Polynomial([1, -1])
        p3 = p1 + p2
        self.assertEqual(p3.coeffs, [2, 4])
        self.assertEqual(p3.degree, 1)

    def test_add_same_polyn_size(self):
        p1 = Polynomial([float("inf"), float("-inf")])
        p2 = Polynomial([float("inf"), float("-inf")])
        self.assertRaises(TypeError, p1.__add__, p2)

    def test_add_different_polyn_size_first_larger(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 2])
        p3 = p1 + p2
        self.assertEqual(p3.coeffs, [1, 3, 5])
        self.assertEqual(p3.degree, 2)

    def test_add_negative_values(self):
        p1 = Polynomial([1, -1])
        p2 = Polynomial([-1, 1])
        p3 = p1 + p2
        self.assertEqual(p3.coeffs, [0])
        self.assertEqual(p3.degree, 0)

    def test_add_incorrect_constant(self):
        p1 = Polynomial([1, 2])
        self.assertRaises(TypeError, p1.__add__, "11")


    def test_add_zero_degree_polynom(self):
        p1 = Polynomial([1, 2])
        p2 = Polynomial([1])
        p3 = p1 + p2
        self.assertEqual(p3.coeffs, [1, 3])
        self.assertEqual(p3.degree, 1)

    def test_mul_same_polyn_size(self):
        p1 = Polynomial([1, 1])
        p2 = Polynomial([1, 1])
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [1, 2, 1])
        self.assertEqual(p3.degree, 2)

    def test_mul_different_polyn_size(self):
        p1 = Polynomial([1, 1, 1])
        p2 = Polynomial([1, 1])
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [1, 2, 2, 1])
        self.assertEqual(p3.degree, 3)


    def test_mul_negative_values(self):
        p1 = Polynomial([1, -1, 1])
        p2 = Polynomial([-1, 1])
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [-1, 2, -2, 1])
        self.assertEqual(p3.degree, 3)

    def test_mul_zero_constant(self):
        p1 = Polynomial([1, 2])
        p2 = 0
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [0])
        self.assertEqual(p3.degree, 0)


    def test_mul_one_value_constant(self):
        p1 = Polynomial([1, 2])
        p2 = 1
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, p1.coeffs)
        self.assertEqual(p3.degree, 1)

    def test_mul_constant(self):
        p1 = Polynomial([1, 2])
        p2 = 5
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [5, 10])
        self.assertEqual(p3.degree, 1)

    def test_mul_incorrect_constant(self):
        p1 = Polynomial([1, 2])
        self.assertRaises(TypeError, p1.__mul__, "5")

    def test_str(self):
        p1 = Polynomial([2, 4])
        self.assertEqual(str(p1), '2x+4')

    def test_str_first_value_is_one(self):
        p1 = Polynomial([1, -1])
        self.assertEqual(str(p1), 'x-1')

    def test_str_all_values_are_one(self):
        p1 = Polynomial([1, 1, 1])
        self.assertEqual(str(p1), 'x2+x+1')

    def test_str_first_two_value_is_zero(self):
        p1 = Polynomial([0, 0, 1])
        self.assertEqual(str(p1), '1')

    def test_str_one_value_is_zero(self):
        p1 = Polynomial([0, 1, 0])
        self.assertEqual(str(p1), 'x')

    def test_str_first_value_is_negative(self):
        p1 = Polynomial([-1, 1, 0])
        self.assertEqual(str(p1), '-x2+x')

    def test_eq_inf_true(self):
        p1 = Polynomial([float("inf"), float("-inf")])
        self.assertTrue(str(p1), 'infx-inf')

    def test_str_float(self):
        p1 = Polynomial([-1.1, 1.9, 0])
        self.assertEqual(str(p1), '-1.1x2+1.9x')

if __name__ == "__main__":
    unittest.main()