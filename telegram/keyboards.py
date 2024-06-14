from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

_IKB = InlineKeyboardButton
_RKM = ReplyKeyboardMarkup
_IKM = InlineKeyboardMarkup
_KB = KeyboardButton
_RKR = ReplyKeyboardRemove

_menu = [
    [
        _IKB(text="Алгебра", callback_data="algebra"),
        _IKB(text="Графики", callback_data="graphics"),
    ]
]
menu = _IKM(inline_keyboard=_menu)

# exit_kb = _RKM(keyboard=[[_KB(text="< Выйти в меню")]], resize_keyboard=True)
iexit_kb = _IKM(
    inline_keyboard=[[_IKB(text="<< К выбору режима", callback_data="to_main")]]
)

_algebra = [
    [_IKB(text="Калькулятор", callback_data="calc")],
    [_IKB(text="Значение функции в точке", callback_data="fvp")],
    [_IKB(text="Число к научному виду", callback_data="to_scientific")],
    [_IKB(text="Неопр. Интеграл", callback_data="undefind_integral")],
    [_IKB(text="Определенный интеграл", callback_data="integral")],
    [_IKB(text="СКО", callback_data="std")],
    [_IKB(text="Среднее значение", callback_data="mean")],
    [_IKB(text="Производная", callback_data="derr")],
    [_IKB(text="<< К выбору режима", callback_data="to_main")],
]
algebra = _IKM(inline_keyboard=_algebra)

_graphics = [
    [_IKB(text="Интерполяция", callback_data="interp")],
    [_IKB(text="Аппроксимация", callback_data="approx")],
    [_IKB(text="График функции", callback_data="simple")],
    [_IKB(text="<< К выбору режима", callback_data="to_main")],
]
graphics = _IKM(inline_keyboard=_graphics)

_go_back_to_algebra = [
    [_IKB(text="< Назад", callback_data="algebra")],
    [_IKB(text="<< К выбору режима", callback_data="to_main")],
]
go_back_to_algebra = _IKM(inline_keyboard=_go_back_to_algebra)

_go_back_to_graphs = [
    [_IKB(text="< Назад", callback_data="graphics")],
    [_IKB(text="<< К выбору режима", callback_data="to_main")],
]
go_back_to_graphs = _IKM(inline_keyboard=_go_back_to_graphs)

_need_to_optimise = [[_IKB(text="оптимизировать", callback_data="optimise")]]
need_to_optimise = _IKM(inline_keyboard=_need_to_optimise)
