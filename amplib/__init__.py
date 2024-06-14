from .calcs import calc
from .functions import function_substitution
from .graphics import interpolate, approximate, simple
from .integrals import definite_integral, finite_integral
from .numeric import to_scientific, mean, std
from .diff import derrivate
from .tools import (
    SPEC_FUNCTIONS,
    SPEC_SYMBOLS,
    BASE_NUMBERS,
    REPLACE_FUNCTIONS,
    newlined_with_variables,
    newlined_without_variables,
    newlined_without_variables_param,
    to_float,
    interp_separator,
    approx_separator,
    find_variables,
)

__all__ = [
    # calcs
    "calc",
    # functions
    "function_substitution",
    # graphics
    "interpolate",
    "approximate",
    "simple",
    # integrals
    "definite_integral",
    "finite_integral",
    # numeric
    "to_scientific",
    "mean",
    "std",
    # diff
    "derrivate",
    #
    #  ________________ tools ________________
    #
    # symbols
    "SPEC_FUNCTIONS",
    "SPEC_SYMBOLS",
    "BASE_NUMBERS",
    "REPLACE_FUNCTIONS",
    # separators
    "newlined_with_variables",
    "newlined_without_variables",
    "newlined_without_variables_param",
    "to_float",
    "interp_separator",
    "approx_separator",
    # searchers
    "find_variables",
]
