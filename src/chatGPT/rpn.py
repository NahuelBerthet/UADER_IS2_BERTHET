"""
Calculadora Reverse Polish Notation (RPN).

Características:
- Soporta enteros y floats
- Operadores: + - * /
- Funciones matemáticas
- Trigonometría en grados
- Comandos de pila
- 10 memorias (00–09)

Uso:
    python rpn.py "3 4 +"
"""

import math
import operator
import sys


class RPNError(Exception):
    """Error específico de la calculadora RPN."""


def pop(stack, n=1):
    """Extrae uno o dos valores de la pila."""
    if len(stack) < n:
        raise RPNError("pila insuficiente para operar")

    if n == 1:
        return stack.pop()

    b = stack.pop()
    a = stack.pop()
    return a, b


OPS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

CONST = {
    "p": math.pi,  # π
    "e": math.e,  # número de Euler
    "j": (1 + math.sqrt(5)) / 2,  # razón áurea
}

FUNC = {
    "sqrt": math.sqrt,
    "log": math.log10,
    "ln": math.log,
    "ex": math.exp,
    "10x": lambda x: 10**x,
}


def sin_deg(x):
    return math.sin(math.radians(x))


def cos_deg(x):
    return math.cos(math.radians(x))


def tan_deg(x):
    return math.tan(math.radians(x))


def asin_deg(x):
    return math.degrees(math.asin(x))


def acos_deg(x):
    return math.degrees(math.acos(x))


def atan_deg(x):
    return math.degrees(math.atan(x))


TRIG = {
    "sin": sin_deg,
    "cos": cos_deg,
    "tg": tan_deg,
    "asin": asin_deg,
    "acos": acos_deg,
    "atg": atan_deg,
}


def op_bin(stack, op):
    """Aplica operador binario."""
    a, b = pop(stack, 2)

    if op == "/" and b == 0:
        raise RPNError("división por cero")

    stack.append(OPS[op](a, b))


def op_func(stack, func):
    """Aplica función matemática."""
    try:
        stack.append(FUNC[func](pop(stack)))
    except ValueError as err:
        raise RPNError(str(err)) from err


def op_trig(stack, func):
    """Aplica función trigonométrica."""
    try:
        stack.append(TRIG[func](pop(stack)))
    except ValueError as err:
        raise RPNError(str(err)) from err


def op_extra(stack, token):
    """Operaciones especiales."""
    if token == "yx":
        a, b = pop(stack, 2)
        stack.append(a**b)
        return True

    if token == "1/x":
        x = pop(stack)
        if x == 0:
            raise RPNError("división por cero")
        stack.append(1 / x)
        return True

    if token.lower() == "chs":
        stack.append(-pop(stack))
        return True

    return False


def cmd_stack(stack, cmd):
    """Manipulación de pila."""
    if cmd == "dup":
        value = pop(stack)
        stack.extend([value, value])

    elif cmd == "swap":
        a, b = pop(stack, 2)
        stack.extend([b, a])

    elif cmd == "drop":
        pop(stack)

    else:  # clear
        stack.clear()


def cmd_mem(stack, memory, cmd):
    """Operaciones de memoria."""
    index = int(pop(stack))

    if not 0 <= index <= 9:
        raise RPNError("memoria inválida (00-09)")

    if cmd == "STO":
        memory[index] = pop(stack)
    else:
        stack.append(memory[index])


def evaluar(expr):
    """Evalúa una expresión RPN."""
    if not expr.strip():
        raise RPNError("expresión vacía")

    stack = []
    memory = [0.0] * 10

    for token in expr.split():

        # número
        try:
            stack.append(float(token))
            continue
        except ValueError:
            pass

        if token in CONST:
            stack.append(CONST[token])
            continue

        if token in OPS:
            op_bin(stack, token)
            continue

        if token in FUNC:
            op_func(stack, token)
            continue

        if token in TRIG:
            op_trig(stack, token)
            continue

        if op_extra(stack, token):
            continue

        if token in {"dup", "swap", "drop", "clear"}:
            cmd_stack(stack, token)
            continue

        if token in {"STO", "RCL"}:
            cmd_mem(stack, memory, token)
            continue

        raise RPNError(f"token inválido: {token}")

    if len(stack) != 1:
        raise RPNError("la expresión debe dejar exactamente 1 valor en la pila")

    return stack[0]


def main():
    """Punto de entrada del programa."""
    expr = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input()

    try:
        print(evaluar(expr))
    except RPNError as err:
        print("Error:", err)


if __name__ == "__main__":
    main()