from .errors import ConvertError, InputError, SizeMissmatchError


def newlined_with_variables(function) -> dict:
    def wrapped(input: str, name_param=None):
        sep = ";"
        input = input.split("\n")
        tree = {}
        for line in input:
            parts = line.split(sep)
            target = parts[0]

            try:
                values = parts[1]
            except IndexError:
                return InputError(line)

            target = "".join(target.split())
            if target in tree.keys():
                tree[target] += [values.split()]
            else:
                tree[target] = [values.split()]

        if name_param is None:
            response = function(tree)
        else:
            response = function(tree, name_param)
        return response

    return wrapped


def newlined_without_variables(function) -> list:
    def wrapped(input: str):
        sep = "\n"
        input = input.split(sep)
        for i, expr in enumerate(input):
            input[i] = "".join(expr.split())

        response = function(input)
        return response

    return wrapped


def newlined_without_variables_param(function) -> str:
    def wrapped(input: str, param: str):
        sep = "\n"
        input = input.split(sep)
        for i, expr in enumerate(input):
            input[i] = "".join(expr.split())

        response = function(input, param)
        return response

    return wrapped


def to_float(function) -> list:
    def wrapped(input: str):
        values = input.split()

        for i, value in enumerate(values):
            try:
                values[i] = float(value)
            except ValueError:
                err = ConvertError(value)
                return err

        response = function(values)
        return response

    return wrapped


def interp_separator(function) -> str:
    def wrapped(input: str, name_param: str):
        input = input.split("\n")
        final_set_of_points = {"x": [], "y": []}
        for set_of_points in input:
            final_set_of_points["x"] += [set_of_points.split(";")[0].split()]
            final_set_of_points["y"] += [set_of_points.split(";")[1].split()]

        for i, sub_set in enumerate(final_set_of_points["x"]):
            if len(sub_set) != len(final_set_of_points["y"][i]):
                return SizeMissmatchError(sub_set, final_set_of_points["y"][i])

        sub_array = final_set_of_points["x"]
        for i, sub_list in enumerate(sub_array):
            for j, point in enumerate(sub_list):
                try:
                    sub_array[i][j] = float(point)
                except ValueError as ve:
                    err = ConvertError(point)
                    return err

        sub_array = final_set_of_points["y"]
        for i, sub_list in enumerate(sub_array):
            for j, point in enumerate(sub_list):
                try:
                    sub_array[i][j] = float(point)
                except ValueError as ve:
                    err = ConvertError(point)
                    return err

        final_set_of_points["param"] = name_param

        response = function(final_set_of_points)

        return response

    return wrapped


def approx_separator(function) -> str:
    def wrapped(input: str, name_param: str):
        input = input.split("\n")
        final_set_of_points = {"x": [], "y": [], "degree": []}
        for set_of_points in input:
            if set_of_points.count(";") == 1:
                final_set_of_points["x"] += [set_of_points.split(";")[0].split()]
                final_set_of_points["y"] += [set_of_points.split(";")[1].split()]
                final_set_of_points["degree"].append(1)
            elif set_of_points.count(";") == 2:
                final_set_of_points["x"] += [set_of_points.split(";")[0].split()]
                final_set_of_points["y"] += [set_of_points.split(";")[1].split()]
                try:
                    final_set_of_points["degree"].append(
                        int("".join(set_of_points.split(";")[2].split()))
                    )
                except ValueError as ve:
                    err = ConvertError(set_of_points.split(";")[2])
                    return err
            else:
                err = InputError(set_of_points)
                return err

        for i, sub_set in enumerate(final_set_of_points["x"]):
            if len(sub_set) != len(final_set_of_points["y"][i]):
                return SizeMissmatchError(sub_set, final_set_of_points["y"][i])

        sub_array = final_set_of_points["x"]
        for i, sub_list in enumerate(sub_array):
            for j, point in enumerate(sub_list):
                try:
                    sub_array[i][j] = float(point)
                except ValueError as ve:
                    err = ConvertError(point)
                    return err

        sub_array = final_set_of_points["y"]
        for i, sub_list in enumerate(sub_array):
            for j, point in enumerate(sub_list):
                try:
                    sub_array[i][j] = float(point)
                except ValueError as ve:
                    err = ConvertError(point)
                    return err

        final_set_of_points["param"] = name_param

        response = function(final_set_of_points)

        return response

    return wrapped
