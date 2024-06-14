class ParseError:
    def __init__(self, ve: str) -> None:
        ve = str(ve)
        s = ve.find("'") + 1
        e = ve.rfind("'")
        self.e = "ERROR: " + ve[s:e]

    def __str__(self) -> str:
        return self.e


class AMPBaseError:
    def __init__(self, err) -> None:
        self.e = "ERROR: {err}".format(err=err)

    def __str__(self) -> str:
        return self.e


class ConvertError(AMPBaseError):
    def __init__(self, variable) -> None:
        err = "can't convert '{type}' to 'float' : {variable}".format(
            type=type(variable), variable=variable
        )
        super().__init__(err)


class EmptyVariableError(AMPBaseError):
    def __init__(self, function) -> None:
        err = (
            "failed to identify the variables in the equation\n[\n{function}\n]".format(
                function=function
            )
        )
        super().__init__(err)


class MissmatchVariableError(AMPBaseError):
    def __init__(self, function, variable, arguments=None) -> None:
        if arguments is None:
            err = "incorrect input: {function} : var -> {variable}".format(
                function=function, variable=variable
            )
        else:
            err = (
                "incorrect input: {function} : {arguments} : var -> {variable}".format(
                    function=function, arguments=arguments, variable=variable
                )
            )
        super().__init__(err)


class VariableError(AMPBaseError):
    def __init__(self, function, variable, arguments=None) -> None:
        if arguments is None:
            err = "can't use '{variable}' as a variable: {function} : var -> {variable}".format(
                variable=variable, function=function
            )
        else:
            err = "can't use '{variable}' as a variable: {function} : {arguments} : var -> {variable}".format(
                variable=variable, function=function, arguments=arguments
            )
        super().__init__(err)


class InputError(AMPBaseError):
    def __init__(self, line) -> None:
        err = "incorrect input: {line}".format(line=line)
        super().__init__(err)


class EmptyInputError(AMPBaseError):
    def __init__(self) -> None:
        err = f"input is empty"
        super().__init__(err)


class SizeMissmatchError(AMPBaseError):
    def __init__(self, list1, list2) -> None:
        err = (
            "size {list1} is not the same as size {list2} : ({size1}, {size2})".format(
                list1=list1,
                list2=list2,
                size1=len(list1),
                size2=len(list2),
            )
        )
        super().__init__(err)
