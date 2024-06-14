from aiogram.fsm.state import StatesGroup, State


menu_state = State()


class General(StatesGroup):
    algebra_state = State()
    graphs_state = State()
    donate_state = State()


class Algebra(StatesGroup):
    calc_state = State()
    fvp_state = State()
    to_scientific_state = State()
    undefind_integral_state = State()
    defined_integral_state = State()
    derr_state = State()
    std_state = State()
    mean_state = State()


class Graphics(StatesGroup):
    interp_state = State()
    approx_state = State()
    simple_state = State()
