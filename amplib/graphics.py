from .tools import (
    interp_separator,
    approx_separator,
    newlined_without_variables_param,
    find_variables,
    REPLACE_FUNCTIONS,
)
from .tools.errors import InputError

import os

import matplotlib.pyplot as plt
from matplotlib.axes import _axes
import numpy as np
from scipy.interpolate import Rbf
from sympy import N
from numexpr import evaluate


def deg_to_rad(x):
    return x * np.pi / 180


def rad_to_deg(x):
    return x * 180 / np.pi


def finalize(ax: _axes.Axes, g_type: str, name_param: str) -> str:
    ax2 = ax.secondary_xaxis("top", functions=(rad_to_deg, deg_to_rad))
    ax.legend()
    ax.set_xlabel("X (radians)")
    ax2.set_xlabel("X (degrees)")
    ax.set_ylabel("$Y$")
    ax2.set_xlim(ax.get_xlim())

    if f"{name_param}" in os.listdir("temporary_storage_of_graphics"):
        plt.savefig(f"temporary_storage_of_graphics/{name_param}/{g_type}.png")
    else:
        os.mkdir(f"temporary_storage_of_graphics/{name_param}")
        plt.savefig(f"temporary_storage_of_graphics/{name_param}/{g_type}.png")
    plt.close("all")

    return f"temporary_storage_of_graphics/{name_param}/{g_type}.png"


@interp_separator
def interpolate(points: dict) -> tuple:
    fig, ax = plt.subplots()
    ax: _axes.Axes
    ax.grid(True)

    for i in range(len(points["x"])):
        rbf = Rbf(points["x"][i], points["y"][i])
        x_plot = np.linspace(points["x"][i][0], points["x"][i][-1])
        y_plot = rbf(x_plot)
        ax.plot(x_plot, y_plot, label=f"$y = f_{i + 1}(x)$")
        ax.scatter(points["x"][i], points["y"][i])

    name = finalize(ax, "INTERPOLATION", points["param"])

    return name


@approx_separator
def approximate(points: dict) -> tuple:
    fig, ax = plt.subplots()
    ax: _axes.Axes
    ax.grid(True)

    plot_description = ""
    for i in range(len(points["x"])):
        coef = np.polyfit(points["x"][i], points["y"][i], points["degree"][i])
        f = np.poly1d(coef)
        x_plot = np.linspace(points["x"][i][0], points["x"][i][-1])
        y_plot = f(x_plot)
        ax.plot(x_plot, y_plot, label=f"$y = f_{i + 1}^{points['degree'][i]}(x)$")
        ax.scatter(points["x"][i], points["y"][i])
        sub_plot_description = ""
        for i, c in enumerate(coef):
            if i == 0:
                sub_plot_description += f"{round(c, 4)} * x^{len(coef) - i - 1}"
            elif len(coef) == i + 1:
                sub_plot_description += f" + {round(c, 4)}"
            else:
                sub_plot_description += f" + {round(c, 4)} * x^{len(coef) - i - 1}"
        plot_description += f"{N(sub_plot_description)}\n"

    name = finalize(ax, "APPROXIMATION", points["param"])

    return name, plot_description


@newlined_without_variables_param
def simple(exprs: list[str], name_param: str) -> str:
    name = None
    for i, function in enumerate(exprs):
        for f in REPLACE_FUNCTIONS.keys():
            if f in function:
                exprs[i] = exprs[i].replace(f, REPLACE_FUNCTIONS[f])

    fig, ax = plt.subplots()
    ax.grid(True)
    ax: _axes.Axes
    for expr in exprs:
        variable = find_variables(expr)
        if len(variable) != 1:
            return InputError(expr)
        variable = variable[0]
        x = np.linspace(-10, 10, 1000)
        expr = expr.replace("^", "**")
        y = evaluate(expr, local_dict={variable: x})
        ax.plot(x, y, label=f"{expr}")
    ax.legend()
    name = finalize(ax, "SIMPLE", name_param)
    return name
