
from unittest import TestCase
from mathlib import *

class Add(TestCase):
    def test_addBasic(self):
        self.assertEqual(0 ,add(0 ,0))
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
        self.assertEqual( -0.578965, add(1, -1.578965))

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
        self.assertEqual(-1, sub(sub(1,1), 1))
        self.assertEqual(-4, sub(sub(5,8), 1))
        self.assertEqual(-1, sub(sub(1,sub(1,(sub(1,1)))), 1))

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
        self.assertEqual(147, mul(mul(7,3), 7))
        self.assertEqual(mul(mul(7,3), 7), mul(7, mul(7,3)))
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
        self.assertRaises(ValueError, pow, 0,-2)
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
        self.assertEqual(round(1/3,8), root(9, -2))
        self.assertEqual(round(1/3,8), root(27, -3))

