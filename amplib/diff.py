from .tools import newlined_without_variables, find_variables, REPLACE_FUNCTIONS
from .tools.errors import EmptyVariableError, ParseError

from sympy import symbols, diff


@newlined_without_variables
def derrivate(input: list):
    response = ""
    for function in input:
        for f in REPLACE_FUNCTIONS.keys():
            if f in function:
                function: str = function.replace(f, REPLACE_FUNCTIONS[f])

        variables = find_variables(function)
        for variable in variables:
            if variable == "":
                return EmptyVariableError(function)
        variables = symbols(variables)

        for variable in variables:
            try:
                sub_response = diff(function, variable)
            except ValueError as ve:
                err = ParseError(ve)
                return err
            response += f"d[{function}]_[{variable}] = {sub_response}\n"

    return response
