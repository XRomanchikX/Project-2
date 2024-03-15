from aiogram import types
from commands.data_db.States import FormAdmin
from aiogram.fsm.context import FSMContext
import admin_commands.buttons_a as but
from icecream import ic
from commands.data_db.sql.database import sql, db, insert_user_id
from commands.data_db.sql.commands_db import *
from commands.data_db.Googlesheet import *

result = {} # Scores

async def admin_panel(message: types.Message, state: FSMContext):
    await state.clear()
    user_id = message.from_user.id
    if user_id == 1028676957 or user_id == 925098584 or user_id == 864498325:
        await message.answer("Выберите действие", reply_markup=but.get_admin_panel_keyboard())
async def admin_panel_call(callback_query: types.CallbackQuery, state: FSMContext):
    await state.clear()
    user_id = callback_query.from_user.id
    if user_id == 1028676957:
        await callback_query.message.edit_text("Выберите действие", reply_markup=but.get_admin_panel_keyboard())


async def admin_stavka(callback_query: types.CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id
    sql.execute(f"Select id from people where id = {user_id}")
    data = sql.fetchone()
    stavka = worksheet.acell('AS2').value
    await callback_query.message.edit_text(f"Текущая процентная ставка - {stavka}%, хотите её изменить?", reply_markup=but.get_stavka_keyboard())
async def admin_stavka_edit(callback_query: types.CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id
    await callback_query.message.edit_text(f"Введите новую ставку (число)", reply_markup=but.get_cancel_edit_keyboard())
    await state.set_state(FormAdmin.edit_stavka)
async def admin_new_stavka(message: types.Message, state: FSMContext):
    await state.clear()
    print(message.text)
    worksheet.update_cell(2, 45, message.text)
    user_id = message.from_user.id
    stavka = worksheet.acell('AS2').value
    await message.answer(f"Успешно, на данные момент ставка - {stavka}%", reply_markup=but.get_admin_panel_keyboard())


async def admin_result(callback_query: types.CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id
    await callback_query.message.edit_text(f"Выберите действие", reply_markup=but.get_result_keyboard())


