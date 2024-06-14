from .tools import newlined_with_variables, find_variables, REPLACE_FUNCTIONS
from .tools.errors import ParseError, EmptyVariableError
from sympy import N, sympify


@newlined_with_variables
def function_substitution(input: dict):
    response = ""
    for function, values in input.items():
        for f in REPLACE_FUNCTIONS.keys():
            if f in function:
                function: str = function.replace(f, REPLACE_FUNCTIONS[f])

        variables = find_variables(function)

        for variable in variables:
            for sub_values in values:
                if variable == "":
                    return EmptyVariableError(function)

                sub_response = ""
                for val in sub_values:
                    try:
                        expr = sympify(
                            function.replace(variable, val),
                            convert_xor=True,
                            evaluate=True,
                        )
                        result_of_value = N(expr)
                    except ValueError as ve:
                        err = ParseError(ve)
                        return err
                    sub_response += f"{result_of_value}\n"

                response += f"{function} : ({variable}) : [\n{sub_response}]\n"

    return response
