#Unit tests for Farm compiler

import unittest
from farm_compiler import *


class alphabet_testcase(unittest.TestCase):
    def test_01(self):
        self.assertEqual(Farm.compile_f(">+,,!6"), "bbcc")
    def test_02(self):
        self.assertEqual(Farm.compile_f(">>>>,,,,"), "eeee")
    def test_03(self):
        self.assertEqual(Farm.compile_f(">>,<<,>>>>>>!5>>>>!4,"), "cat")
    def test_04(self):
        self.assertEqual(Farm.compile_f(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>,"), "e")
    def test_05(self):
        self.assertEqual(Farm.compile_f(",<,<<,"), "aaa")
    def test_06(self):
        self.assertEqual(Farm.compile_f(">>>?29,>?15,"), "va")
    def test_07(self):
        self.assertEqual(Farm.compile_f(">>>?29,>?15,<<<<<!5,"), "var")
    def test_08(self):
        self.assertEqual(Farm.compile_f(">>>?29,>?15,<<<<<!5,++?24.>>>!3,.+++++?37.-----?37.---!2."), "var x = 5")


if __name__ == '__main__':
    unittest.main()
