from unittest import TestCase, main
from src.mathlib import *

import math

pi = 3.141592653589793

class Add(TestCase):
    def test_addBasic(self):
        self.assertEqual(0, add(0, 0))
        self.assertEqual(1, add(1, 0))
        self.assertEqual(1, add(0, 1))
        self.assertEqual(4, add(4, 0))
        self.assertEqual(4, add(3, 1))
        self.assertEqual(10, add(3, 7))
        self.assertEqual(7, add(3, 4))
        self.assertEqual(7, add(4, 3))

    def test_addEqual(self):
        self.assertEqual(add(1, 0), add(1, 0))
        self.assertEqual(add(0, 1), add(0, 1))
        self.assertEqual(add(5, 1), add(5, 1))
        self.assertEqual(add(5, 1), add(1, 5))
        self.assertEqual(add(7, 1), add(1, 7))

    def test_addNegative(self):
        self.assertEqual(0, add(-2, 2))
        self.assertEqual(1, add(3, -2))
        self.assertEqual(1, add(-2, 3))
        self.assertEqual(-5, add(-5, 0))
        self.assertEqual(-3, add(3, -6))
        self.assertEqual(-10, add(-15, 5))

    def test_addFloat(self):
        self.assertEqual(0, add(0.5, -0.5))
        self.assertEqual(5, add(4.5, 0.5))
        self.assertEqual(-5.5, add(-8.5, 3))
        self.assertEqual(1.422, add(3, -1.578))
        self.assertEqual(-0.578965, add(1, -1.578965))

    def test_addHugeNumber(self):
        self.assertEqual(69101427, add(5847212, 63254215))
        self.assertEqual(150355, add(84523, 65832))
        self.assertEqual(419774, add(321020, 98754))


class Sub(TestCase):
    def test_subBasic(self):
        self.assertEqual(1, sub(1, 0))
        self.assertEqual(4, sub(5, 1))
        self.assertEqual(3, sub(10, 7))
        self.assertEqual(10, sub(15, 5))
        self.assertEqual(0, sub(0, 0))

    def test_subFloat(self):
        self.assertEqual(1.5, sub(1.5, 0))
        self.assertEqual(2, sub(4, 2.0))
        self.assertEqual(0, sub(0.7, 0.7))

    def test_subNegative(self):
        self.assertEqual(-1, sub(-1, 0))
        self.assertEqual(0, sub(-5, -5))
        self.assertEqual(-16.3, sub(-8, 8.3))
        self.assertEqual(1, sub(-2, -3))

    def test_subHugeNumber(self):
        self.assertEqual(893067803, sub(956321457, 63253654))
        self.assertEqual(58690912, sub(52142366, -6548546))

    def test_subMultiple(self):
        self.assertEqual(-1, sub(sub(1, 1), 1))
        self.assertEqual(-4, sub(sub(5, 8), 1))
        self.assertEqual(-1, sub(sub(1, sub(1, (sub(1, 1)))), 1))


class Div(TestCase):
    def test_divBasic(self):
        self.assertEqual(3, div(9, 3))
        self.assertEqual(10, div(100, 10))
        self.assertEqual(1, div(1, 1))
        """self.assertRaises(ZeroDivisionError, div,(2,0))
        self.assertRaises(ZeroDivisionError, div, (0, 0))
        self.assertRaises(ZeroDivisionError, div, (-2, 0))"""

    def test_divNegative(self):
        self.assertEqual(-3, div(9, -3))
        self.assertEqual(-10, div(-100, 10))
        self.assertEqual(3, div(-9, -3))
        self.assertEqual(10, div(-100, -10))

    def test_divFloat(self):
        self.assertEqual(2, div(5, 2.5))
        self.assertEqual(4, div(10, 2.5))
        self.assertEqual(5, div(5.5, 1.1))
        self.assertEqual(2.5, div(5, 2))

    def test_divHugeNumber(self):
        self.assertEqual(1000, div(1500000, 1500))
        self.assertEqual(913.03860302, div(51423659854, 56321452))
        self.assertEqual(3972.32921059, div(251254589.365, 63251.2))


class Mul(TestCase):
    def test_mulBasic(self):
        self.assertEqual(25, mul(5, 5))
        self.assertEqual(10, mul(5, 2))
        self.assertEqual(49, mul(7, 7))
        self.assertEqual(0, mul(0, 5))

    def test_mulFloat(self):
        self.assertEqual(28.6, mul(5.5, 5.2))
        self.assertEqual(13.545, mul(2.15, 6.3))
        self.assertEqual(20.11119137, mul(6.256398, 3.2145))

    def test_mulNegative(self):
        self.assertEqual(-25, mul(5, -5))
        self.assertEqual(-10, mul(-5, 2))
        self.assertEqual(49, mul(-7, -7))
        self.assertEqual(0, mul(0, -5))
        self.assertEqual(28.6, mul(-5.5, -5.2))
        self.assertEqual(-13.545, mul(-2.15, 6.3))
        self.assertEqual(-20.11119137, mul(6.256398, -3.2145))

    def test_mulHugeNumber(self):
        self.assertEqual(2059673287505292, mul(56365698, 36541254))
        self.assertEqual(7671495544846154583, mul(23569896563, 325478541))

    def test_mulMultiple(self):
        self.assertEqual(147, mul(mul(7, 3), 7))
        self.assertEqual(mul(mul(7, 3), 7), mul(7, mul(7, 3)))
        self.assertEqual(0, mul(mul(7, mul(mul(7, mul(7, 3)), 0)), mul(7, 3)))


class Fact(TestCase):
    def test_factBasic(self):
        self.assertEqual(1, fact(1))
        self.assertEqual(1, fact(0))
        self.assertRaises(ValueError, fact, -10)

    def test_factHugeNumber(self):
        self.assertEqual(479001600, fact(12))
        self.assertEqual(121645100408832000, fact(19))


class Pow(TestCase):
    def test_powBasic(self):
        self.assertEqual(0, pow(0, 2))
        self.assertEqual(2, pow(2, 1))
        self.assertEqual(8, pow(2, 3))
        self.assertEqual(27, pow(3, 3))

    def test_powNegativeFloat(self):
        self.assertRaises(ValueError, pow, 0, -2)
        self.assertRaises(ValueError, pow, 0, -10)
        self.assertEqual(0.25, pow(2, -2))
        self.assertEqual(0.5, pow(2, -1))
        self.assertEqual(0.125, pow(2, -3))
        self.assertEqual(-27, pow(-3, 3))
        self.assertEqual(-8, pow(-2, 3))

    def test_powHugeNumber(self):
        self.assertEqual(857375, pow(95, 3))
        self.assertEqual(90859024, pow(9532, 2))


class Root(TestCase):
    def test_rootBasic(self):
        self.assertEqual(3, root(9, 2))
        self.assertEqual(3, root(27, 3))
        self.assertEqual(2, root(2, 1))

    def test_rootNegativeFloat(self):
        self.assertRaises(ValueError, root, -10, 2)
        self.assertRaises(ValueError, root, -10, -5)
        self.assertEqual(round(1 / 3, 8), root(9, -2))
        self.assertEqual(round(1 / 3, 8), root(27, -3))


class Mod(TestCase):
    def test_modBasic(self):
        self.assertEqual(0, mod(0, 1))
        self.assertEqual(0, mod(0, -1))
        self.assertEqual(0, mod(5, 1))
        self.assertEqual(1, mod(7, 2))
        self.assertEqual(1, mod(10, 3))
        self.assertEqual(15, mod(143, 32))
        self.assertEqual(2, mod(198, 14))

    def test_modNegative(self):
        self.assertEqual(-1, mod(7, -2))
        self.assertEqual(-2, mod(10, -3))
        self.assertEqual(17, mod(-143, 32))
        self.assertEqual(-2, mod(-198, -14))

    def test_modFloatErr(self):
        self.assertRaises(ValueError, mod, 0, 1.45)
        self.assertRaises(ValueError, mod, 22, 11.8)
        self.assertRaises(ValueError, mod, 1.6, 33)
        self.assertRaises(ValueError, mod, 9.47, 131.141)

class Sin(TestCase):
    def test_sinBasic(self):
        self.assertEqual(-0.95892427,sin(5))
        self.assertEqual(0, sin(0))
        self.assertEqual(0.84147098, sin(1))
        self.assertEqual(0.90929743, sin(2))

    def test_sinPi(self):
        self.assertEqual(0,sin(2*math.pi))
        self.assertEqual(0, sin(4 * math.pi))
        self.assertEqual(0, sin(1 * math.pi))
        self.assertEqual(-1, sin(3.5 * math.pi))
        self.assertEqual(1, sin(2.5 * math.pi))
        #self.assertEqual(1, sin(3 * math.pi))

class Cos(TestCase):
    def test_cosBasic(self):
        self.assertEqual(0.28366219, cos(5))
        self.assertEqual(1, cos(0))
        self.assertEqual(0.54030231, cos(1))
        self.assertEqual(-0.41614684, cos(2))


    def test_cosPi(self):
        self.assertEqual(1, cos(2 * math.pi))
        self.assertEqual(1, cos(4 * math.pi))
        self.assertEqual(-1, cos(1 * math.pi))
        self.assertEqual(0, cos(3.5 * math.pi))
        self.assertEqual(0, cos(2.5 * math.pi))

class Tan(TestCase):
    def test_tanBasic(self):
        self.assertEqual(-3.38051494, tan(5))
        self.assertEqual(0, tan(0))
        self.assertEqual(1.5574077, tan(1))
        self.assertEqual(-2.18503985, tan(2))
       
if __name__ == "__main__":
    main()
