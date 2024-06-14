import os

from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

from aiogram import flags
from aiogram.fsm.context import FSMContext
from aiogram.types.callback_query import CallbackQuery

from texts import text
import keyboards
from states import General, Algebra, Graphics, menu_state

import amplib as amp

router = Router()


@router.message(Command("start"))
async def start(message: Message):
    user_name = message.from_user.full_name
    await message.answer(
        text["start"].format(user_name=user_name), reply_markup=keyboards.menu
    )


@router.message(Command("menu"))
async def return_to_menu(message: Message, state: FSMContext):
    await state.set_state(menu_state)
    await message.answer(text["menu"], reply_markup=keyboards.menu)


@router.callback_query(F.data == "to_main")
async def menu(clback: CallbackQuery, state: FSMContext):
    await state.set_state(menu_state)
    await clback.message.delete()
    await clback.message.answer(text["menu"], reply_markup=keyboards.menu)


# ___________________________MODES___________________________


@router.callback_query(F.data == "algebra")
async def algebra(clback: CallbackQuery, state: FSMContext):
    await state.set_state(General.algebra_state)
    await clback.message.delete()
    await clback.message.answer(
        text["modes"]["algebra"], reply_markup=keyboards.algebra
    )


@router.callback_query(F.data == "graphics")
async def graphs(clback: CallbackQuery, state: FSMContext):
    await state.set_state(General.graphs_state)
    await clback.message.delete()
    await clback.message.answer(
        text["modes"]["graphics"], reply_markup=keyboards.graphics
    )


# ___________________________STATE_CHANGERS___________________________


@router.callback_query(F.data == "calc")
async def calc(clback: CallbackQuery, state: FSMContext):
    await state.set_state(Algebra.calc_state)
    await clback.message.delete()
    await clback.message.answer(text["calc"], reply_markup=keyboards.go_back_to_algebra)


@router.callback_query(F.data == "fvp")
async def func_val_in_point(clback: CallbackQuery, state: FSMContext):
    await state.set_state(Algebra.fvp_state)
    await clback.message.delete()
    await clback.message.answer(text["fvp"], reply_markup=keyboards.go_back_to_algebra)


@router.callback_query(F.data == "to_scientific")
async def to_scientific(clback: CallbackQuery, state: FSMContext):
    await state.set_state(Algebra.to_scientific_state)
    await clback.message.delete()
    await clback.message.answer(
        text["to_scientific"], reply_markup=keyboards.go_back_to_algebra
    )


@router.callback_query(F.data == "undefind_integral")
async def undefind_integral(clback: CallbackQuery, state: FSMContext):
    await state.set_state(Algebra.undefind_integral_state)
    await clback.message.edit_text(
        text["undefind_integral"], reply_markup=keyboards.go_back_to_algebra
    )


@router.callback_query(F.data == "integral")
async def integral(clback: CallbackQuery, state: FSMContext):
    await state.set_state(Algebra.defined_integral_state)
    await clback.message.delete()
    await clback.message.answer(
        text["integral"], reply_markup=keyboards.go_back_to_algebra
    )


@router.callback_query(F.data == "std")
async def std(clback: CallbackQuery, state: FSMContext):
    await state.set_state(Algebra.std_state)
    await clback.message.delete()
    await clback.message.answer(text["std"], reply_markup=keyboards.go_back_to_algebra)


@router.callback_query(F.data == "mean")
async def mean(clback: CallbackQuery, state: FSMContext):
    await state.set_state(Algebra.mean_state)
    await clback.message.delete()
    await clback.message.answer(text["mean"], reply_markup=keyboards.go_back_to_algebra)


@router.callback_query(F.data == "derr")
async def derr(clback: CallbackQuery, state: FSMContext):
    await state.set_state(Algebra.derr_state)
    await clback.message.delete()
    await clback.message.answer(text["derr"], reply_markup=keyboards.go_back_to_algebra)


@router.callback_query(F.data == "interp")
async def interp(clback: CallbackQuery, state: FSMContext):
    await state.set_state(Graphics.interp_state)
    await clback.message.delete()
    await clback.message.answer(
        text["interp"], reply_markup=keyboards.go_back_to_graphs
    )


@router.callback_query(F.data == "approx")
async def approx(clback: CallbackQuery, state: FSMContext):
    await state.set_state(Graphics.approx_state)
    await clback.message.delete()
    await clback.message.answer(
        text["approx"], reply_markup=keyboards.go_back_to_graphs
    )


@router.callback_query(F.data == "simple")
async def simple(clback: CallbackQuery, state: FSMContext):
    await state.set_state(Graphics.simple_state)
    await clback.message.delete()
    await clback.message.answer(
        text["simple"], reply_markup=keyboards.go_back_to_graphs
    )


# ___________________________RETURNERS___________________________


@router.callback_query(F.data == "optimise")
async def optimise(clback: CallbackQuery, state: FSMContext):
    await clback.message.edit_text(text["handling"])
    response = amp.to_scientific(clback.message.text)
    if type(response) is not str:
        response = response.__str__()
    await clback.message.edit_text(response, reply_markup=keyboards.go_back_to_algebra)


@router.message(Algebra.calc_state)
@flags.chat_action("typing")
async def calc(message: Message):
    sub_message = await message.answer(text["handling"])
    response = amp.calc(message.text)
    if type(response) is not str:
        response = response.__str__()
    await sub_message.edit_text(response, reply_markup=keyboards.need_to_optimise)


@router.message(Algebra.fvp_state)
@flags.chat_action("typing")
async def function_substitution(message: Message):
    sub_message = await message.answer(text["handling"])
    response = amp.function_substitution(message.text)
    if type(response) is not str:
        response = response.__str__()
    await sub_message.edit_text(response, reply_markup=keyboards.go_back_to_algebra)


@router.message(Algebra.to_scientific_state)
@flags.chat_action("typing")
async def to_scientific(message: Message):
    sub_message = await message.answer(text["handling"])
    response = amp.to_scientific(message.text)
    if type(response) is not str:
        response = response.__str__()
    await sub_message.edit_text(response, reply_markup=keyboards.go_back_to_algebra)


@router.message(Algebra.undefind_integral_state)
@flags.chat_action("typing")
async def undefind_integral(message: Message):
    sub_message = await message.answer(text["handling"])
    response = amp.definite_integral(message.text)
    if type(response) is not str:
        response = response.__str__()
    await sub_message.edit_text(response, reply_markup=keyboards.go_back_to_algebra)


@router.message(Algebra.defined_integral_state)
@flags.chat_action("typing")
async def defined_integral(message: Message):
    sub_message = await message.answer(text["handling"])
    print("integral")
    response = amp.finite_integral(message.text)
    if type(response) is not str:
        response = response.__str__()
    await sub_message.edit_text(response, reply_markup=keyboards.go_back_to_algebra)


@router.message(Algebra.std_state)
@flags.chat_action("typing")
async def std(message: Message):
    sub_message = await message.answer(text["handling"])
    response = amp.std(message.text)
    if type(response) is not str:
        response = response.__str__()
    await sub_message.edit_text(response, reply_markup=keyboards.need_to_optimise)


@router.message(Algebra.mean_state)
@flags.chat_action("typing")
async def mean(message: Message):
    sub_message = await message.answer(text["handling"])
    response = amp.mean(message.text)
    if type(response) is not str:
        response = response.__str__()
    await sub_message.edit_text(response, reply_markup=keyboards.need_to_optimise)


@router.message(Algebra.derr_state)
@flags.chat_action("typing")
async def derr(message: Message):
    sub_message = await message.answer(text["handling"])
    response = amp.derrivate(message.text)
    if type(response) is not str:
        response = response.__str__()
    await sub_message.edit_text(response, reply_markup=keyboards.go_back_to_algebra)


@router.message(Graphics.interp_state)
@flags.chat_action("typing")
async def interp(message: Message):
    sub_message = await message.answer(text["handling"])
    response = amp.interpolate(message.text, message.chat.username)
    if type(response) is not str:
        response = response.__str__()
        return await sub_message.edit_text(response)
    await sub_message.answer_photo(types.FSInputFile(response))
    await message.delete()
    os.remove(response)


@router.message(Graphics.approx_state)
@flags.chat_action("typing")
async def approx(message: Message):
    sub_message = await message.answer(text["handling"])
    response = amp.approximate(message.text, message.chat.username)
    if len(response) != 2:
        response = response.__str__()
        return await sub_message.edit_text(response)
    await sub_message.answer_photo(
        types.FSInputFile(response[0]), reply_markup=keyboards.go_back_to_graphs
    )
    await sub_message.edit_text(response[1])
    await message.delete()
    os.remove(response[0])


@router.message(Graphics.simple_state)
@flags.chat_action("typing")
async def simple(message: Message):
    sub_message = await message.answer(text["handling"])
    response = amp.simple(message.text, message.chat.username)
    if type(response) is not str:
        response = response.__str__()
        return await sub_message.edit_text(response)
    await sub_message.answer_photo(types.FSInputFile(response))
    await message.delete()
    os.remove(response)
