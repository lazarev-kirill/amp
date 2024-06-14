from .tools import to_float
from .tools.errors import EmptyInputError
from sympy import N
from numpy import mean as np_mean, std as np_std


def delete_exp(number: str, exp_type: str) -> str:
    parts = number.split(exp_type)
    whole = parts[0]
    frac = parts[1]
    if "+" in frac:
        frac = frac.replace("+", "")
    number = f"{whole}*10^({frac})"
    return number


@to_float
def to_scientific(values: list):
    scientific_form = []
    for val in values:
        number = str(N(val, 3))
        if "e" in number:
            number = delete_exp(number, "e")
        elif "E" in number:
            number = delete_exp(number, "E")
        if number[-1] == ".":
            number = number.replace(".", "")
            number = N(f"{number}/100", 3)
            number = f"{number}*10^(2)"
        scientific_form.append(number)
    if len(scientific_form) == 0:
        return EmptyInputError()
    return "\n".join(scientific_form)


@to_float
def mean(values: list):
    response = np_mean(values)
    return f"{response}"


@to_float
def std(values: list):
    response = np_std(values)
    return f"{response}"
