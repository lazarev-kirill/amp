from sympy import sympify, N

from .tools import newlined_without_variables, REPLACE_FUNCTIONS
from .tools.errors import ParseError


@newlined_without_variables
def calc(input: str) -> str:
    response = ""
    for expr in input:
        for f in REPLACE_FUNCTIONS.keys():
            if f in expr:
                expr = expr.replace(f, REPLACE_FUNCTIONS[f])
        try:
            expr = sympify(expr, convert_xor=True, evaluate=True)
            out = N(expr)
        except ValueError as ve:
            err = ParseError(ve)
            return err
        response += f"{out}\n"

    return response
