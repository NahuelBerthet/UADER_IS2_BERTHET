import math
import unittest

from rpn import RPNError, evaluar


class TestRPN(unittest.TestCase):
    """Tests funcionales para la calculadora RPN."""

    def check(self, expr, expected, places=7):
        """Helper para comparar resultados."""
        self.assertAlmostEqual(evaluar(expr), expected, places=places)

    # ---------- operaciones básicas ----------
    def test_operaciones_basicas(self):
        casos = [
            ("3 4 +", 7),
            ("8 2 /", 4),
            ("-3 -2 *", 6),
            ("5 1 2 + 4 * + 3 -", 14),
        ]

        for expr, esperado in casos:
            with self.subTest(expr=expr):
                self.assertEqual(evaluar(expr), esperado)

    # ---------- constantes ----------
    def test_constantes(self):
        casos = [
            ("p", math.pi),
            ("e", math.e),
        ]

        for expr, esperado in casos:
            with self.subTest(expr=expr):
                self.check(expr, esperado)

    # ---------- funciones matemáticas ----------
    def test_funciones(self):
        casos = [
            ("9 sqrt", 3),
            ("100 log", 2),
            ("e ln", 1),
            ("1 ex", math.e),
            ("2 10x", 100),
            ("2 3 yx", 8),
            ("4 1/x", 0.25),
        ]

        for expr, esperado in casos:
            with self.subTest(expr=expr):
                self.check(expr, esperado)

    # ---------- trigonometría ----------
    def test_trigonometria(self):
        casos = [
            ("90 sin", 1),
            ("0 cos", 1),
            ("45 tg", 1),
            ("1 asin", 90),
            ("1 acos", 0),
            ("1 atg", 45),
        ]

        for expr, esperado in casos:
            with self.subTest(expr=expr):
                self.check(expr, esperado, places=5)

    # ---------- manipulación de pila ----------
    def test_comandos_pila(self):
        casos = [
            ("5 dup *", 25),
            ("3 5 swap -", 2),
            ("3 4 drop", 3),
        ]

        for expr, esperado in casos:
            with self.subTest(expr=expr):
                self.assertEqual(evaluar(expr), esperado)

    def test_clear_error(self):
        with self.assertRaises(RPNError):
            evaluar("3 4 clear")

    # ---------- cambio de signo ----------
    def test_chs(self):
        self.assertEqual(evaluar("5 chs"), -5)

    # ---------- memoria ----------
    def test_memoria(self):
        self.assertEqual(evaluar("10 1 STO 1 RCL"), 10)

    def test_memoria_invalida(self):
        with self.assertRaises(RPNError):
            evaluar("5 15 STO")

    # ---------- errores ----------
    def test_errores_generales(self):
        errores = [
            "3 0 /",  # división por cero
            "0 1/x",  # inverso de cero
            "3 4 hola",  # token inválido
            "+",  # pila insuficiente
            "3 4",  # resultado múltiple
            "",  # expresión vacía
        ]

        for expr in errores:
            with self.subTest(expr=expr):
                with self.assertRaises(RPNError):
                    evaluar(expr)

    # ---------- errores matemáticos ----------
    def test_errores_matematicos(self):
        errores = [
            "-1 sqrt",
            "-10 log",
            "2 asin",
        ]

        for expr in errores:
            with self.subTest(expr=expr):
                with self.assertRaises(RPNError):
                    evaluar(expr)


if __name__ == "__main__":
    unittest.main()
