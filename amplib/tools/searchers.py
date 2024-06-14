from .symbols import SPEC_FUNCTIONS, SPEC_SYMBOLS, BASE_NUMBERS


def find_variables(function: str) -> str:
    function = "".join(function.split())
    for sf in SPEC_FUNCTIONS:
        if sf in function:
            function = function.replace(sf, "")
    for ss in SPEC_SYMBOLS:
        if ss in function:
            function = function.replace(ss, "")
    for bn in BASE_NUMBERS:
        if bn in function:
            function = function.replace(bn, "")
    variables = set(function)
    variables = sorted(variables)
    return variables
