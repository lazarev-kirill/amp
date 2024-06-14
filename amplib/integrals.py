from .tools import (
    newlined_with_variables,
    newlined_without_variables,
    find_variables,
    REPLACE_FUNCTIONS,
)
from .tools.errors import EmptyVariableError, MissmatchVariableError, VariableError

from sympy import integrate, symbols


@newlined_without_variables
def definite_integral(input: list):
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
                sub_response = integrate(function, variable)
            except TypeError:
                return VariableError(function, variable)
            except ValueError:
                return MissmatchVariableError(function, variable)

            response += f"Integ({function})d{variable} = {sub_response} + const\n"

    return response


@newlined_with_variables
def finite_integral(input: dict):
    response = ""
    for function, values in input.items():
        sub_response = ""

        for f in REPLACE_FUNCTIONS.keys():
            if f in function:
                function: str = function.replace(f, REPLACE_FUNCTIONS[f])

        variables = find_variables(function)
        for variable in variables:
            if variable == "":
                return EmptyVariableError(function)
        variables = symbols(variables)

        for variable in variables:
            for sub_values in values:
                if len(sub_values) != 2:
                    return MissmatchVariableError(function, variable, sub_values)
                try:
                    sub_response = integrate(
                        function, (variable, sub_values[0], sub_values[1])
                    )
                except TypeError:
                    return VariableError(function, variable, sub_values)
                except ValueError:
                    return MissmatchVariableError(function, variable, sub_values)

                response += (
                    f"Integ({function})d{variable}: {sub_values} = {sub_response}\n"
                )
    return response
