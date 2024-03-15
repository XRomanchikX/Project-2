from aiogram import types
from commands.data_db.States import Form, ran
from aiogram.fsm.context import FSMContext
from buttonses.buttons import *
from icecream import ic
from commands.data_db.sql.database import sql, db, insert_user_id
from tableForUsers import *
from commands.data_db.sql.commands_db import *
from bank_math import *
from aiogram.filters import Command
from aiogram.types import Update

from aiogram import Bot, types, Router, F

result = {} # Scores
db_ = {}

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.service_account import Credentials
# Укажите путь к вашему файлу ключа JSON
json_keyfile_path = 'account.json'

# Укажите имя вашего файла Google Sheets
scope = ['https://www.googleapis.com/auth/spreadsheets']
credentials = Credentials.from_service_account_file('account.json')
client = gspread.authorize(credentials.with_scopes(scope))
sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1nB8jtKhYRqSY51cT9ZU0fAQkKshGq8hGkrSXUKZvUy0/edit?usp=sharing')
worksheet = sheet.get_worksheet(0)
values = worksheet.get_all_values()

def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list)+1)

def normal_user_row(user_id):
    alls = get_user_data(user_id);formated_alls = [i for i in alls]
    normal_alls = []
    for i in formated_alls:
        if i != None:
            normal_alls.append(i)
        if i == None:
            normal_alls.append('')
    normal_alls.pop(0)
    return normal_alls

router = Router()

#@router.message(Command("test"))
#async def start_mess(message: types.Message, state: FSMContext):
#    await message.answer_poll(question="Выберите варианты ответов:",
#                              options=[
#                                  "Вариант 1",
#                                  "Вариант 2",
#                                  "Вариант 3",
#                                  "Вариант 4"],
#                              allows_multiple_answers=True,
#                              reply_markup=kb_1())
#
#@router.callback_query(F.data == "test")
#async def start_call(call: types.CallbackQuery, state: FSMContext,event_update: Update ):
#    tpm_list = event_update.callback_query.message.poll.options
#    result = [i.voter_count for i in tpm_list]
#    result1 = [i.text for i in tpm_list if i.voter_count == 1]
#    
#    if 1 in result:
#        print(result1)
#    if 1 not in result:
#        print(result)
#    


async def start_command(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(f"Добро пожаловать в опросник", reply_markup=get_start_keyboard())

async def start_questions(callback_query: types.CallbackQuery, state: FSMContext):
    global result
    user_id = callback_query.from_user.id
    await callback_query.answer()
    sql.execute(f"Select id from people where id = {user_id}")
    data = sql.fetchone()
    if data is None:
        insert_user_id(user_id)
        db.commit()
    if f"score_{user_id}" not in result:
        result[f"score_{user_id}"] = 0
    result[f"score_{user_id}"] += 0
    await callback_query.message.answer("1. Ваш пол", reply_markup=get_gender_keyboard()) 

    cell = worksheet.find(f"{user_id}")
    try:  # Проверка пользователя в таблице
        row = cell.row
        print(f"Не создан новый пользователь {row}")
    except: # Создание пользователя в таблице
        next_row = next_available_row(worksheet)
        db_[f'row_{user_id}'] = next_row
        worksheet.update_acell("A{}".format(next_row), f'{user_id}')
        print("Создан новый пользователь")
   
async def process_gender(callback_query: types.CallbackQuery, state: FSMContext):
    gender = callback_query.data
    user_id = callback_query.from_user.id
    if gender == 'gender_male': update_gender(user_id, "Мужской")
    if gender == 'gender_female': update_gender(user_id, "Женский")
    await callback_query.answer()
    await callback_query.message.edit_text("2. Ваш возраст", reply_markup=get_age_keyboard())

async def process_age(callback_query: types.CallbackQuery, state: FSMContext):
   user_id = callback_query.from_user.id
   global result
   if callback_query.data == 'age_less_23':
       result[f"score_{user_id}"] += 20
       update_age(user_id, "Меньше 23")
   elif callback_query.data == 'age_25_45':
       result[f"score_{user_id}"] += 35
       update_age(user_id, "Между 25 и 45")
   elif callback_query.data == 'age_46_55':
       result[f"score_{user_id}"] += 30
       update_age(user_id, "Между 46 и 55")
   elif callback_query.data == 'age_more_56':
       result[f"score_{user_id}"] += -20
       update_age(user_id, "Больше 56")
   await callback_query.answer()
   await callback_query.message.edit_text("3. Семейное положение", reply_markup=get_marital_status_keyboard())

async def process_marital_status(callback_query: types.CallbackQuery, state: FSMContext):
   user_id = callback_query.from_user.id
   global result
   if callback_query.data == 'marital_married':
       result[f"score_{user_id}"] += 35
       update_marital_status(user_id, "Замужем")
   elif callback_query.data == 'marital_divorced':
       result[f"score_{user_id}"] += 20
       update_marital_status(user_id, "Разведен(а)")
   elif callback_query.data == 'marital_single':
       result[f"score_{user_id}"] += 15
       update_marital_status(user_id, "Холост(не замужем)")
   elif callback_query.data == 'marital_widowed':
       result[f"score_{user_id}"] += 15
       update_marital_status(user_id, "Вдовец(вдова)")
   await callback_query.answer()
   await callback_query.message.edit_text( "4. Брачный контракт", reply_markup=get_marriage_contract_keyboard())

async def process_marriage_contract(callback_query: types.CallbackQuery, state: FSMContext):
   user_id = callback_query.from_user.id
   global result
   if callback_query.data == 'marriage_yes':
       result[f"score_{user_id}"] += 35
       update_marriage_contract(user_id, 'Да')
   elif callback_query.data == 'marriage_no':
       result[f"score_{user_id}"] += 20
       update_marriage_contract(user_id, 'Нет')
   await callback_query.answer()
   await callback_query.message.edit_text( "5. Количество членов семьи, с кем проживаете", reply_markup=get_family_members_keyboard())

async def process_family_member(callback_query: types.CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id
    if callback_query.data == 'family_mother':
        update_family_members(user_id, 1)
    elif callback_query.data == 'family_father':
        update_family_members(user_id, 2)
    elif callback_query.data == 'family_brother':
        update_family_members(user_id, 3)
    elif callback_query.data == 'family_sister':
        update_family_members(user_id, 4)
    elif callback_query.data == 'family_spouse':
        update_family_members(user_id, 5)
    await callback_query.answer()
    await callback_query.message.edit_text( "6. Доход супруги(супруга)", reply_markup=get_spouse_keyboard())

async def process_spouse_income(callback_query: types.CallbackQuery, state: FSMContext):
    global result
    user_id = callback_query.from_user.id
    if callback_query.data == 'spouse_income_more_50000':
        result[f"score_{user_id}"] += 35
        update_spouse_income(user_id, "Больше 50000")
    elif callback_query.data == 'spouse_income_30000_50000':
        result[f"score_{user_id}"] += 25
        update_spouse_income(user_id, "Между 30000 и 50000")
    elif callback_query.data == 'spouse_income_less_30000':
        result[f"score_{user_id}"] += 15
        update_spouse_income(user_id, "Меньше 30000")
    await callback_query.answer()
    await callback_query.message.edit_text("7. Образование", reply_markup=get_education_keyboard())

async def process_education(callback_query: types.CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id
    global result
    if callback_query.data == 'education_high':
        result[f"score_{user_id}"] += 35
        update_education(user_id, "Учённая степень")
    elif callback_query.data == 'education_higher':
        result[f"score_{user_id}"] += 25
        update_education(user_id, "Высшее")
    elif callback_query.data == 'education_incomplete':
        result[f"score_{user_id}"] += 0
        update_education(user_id, "Незаконченное высшее")
    elif callback_query.data == 'education_secondary_special':
        result[f"score_{user_id}"] += 0
        update_education(user_id, "Средне-специальное")
    elif callback_query.data == 'education_secondary':
        result[f"score_{user_id}"] += 10
        update_education(user_id, "Среднее")
    await callback_query.answer()
    await callback_query.message.edit_text("8. Адрес места жительства (регистрации):", reply_markup=get_registration_address_keyboard())

async def process_registration_address(callback_query: types.CallbackQuery, state: FSMContext):
    global result
    user_id = callback_query.from_user.id
    if callback_query.data == 'registration_address_yes':
        result[f"score_{user_id}"] += 35
        update_registration_address(user_id, 'Есть')
    else: update_registration_address(user_id, 'Нету')
    await callback_query.answer()
    await callback_query.message.edit_text("9. Адрес места пребывания (фактический):", reply_markup=get_actual_address_keyboard())

async def process_actual_address(callback_query: types.CallbackQuery, state: FSMContext):
    global result
    user_id = callback_query.from_user.id
    if callback_query.data == 'actual_address_village':
        result[f"score_{user_id}"] += 10
        update_actual_address(user_id, 'Село, деревня')
    elif callback_query.data == 'actual_address_city':
        result[f"score_{user_id}"] += 25
        update_actual_address(user_id, 'Город')
    elif callback_query.data == 'actual_address_moscow':
        result[f"score_{user_id}"] += 35
        update_actual_address(user_id, 'Москва')
    elif callback_query.data == 'actual_address_spb':
        result[f"score_{user_id}"] += 30
        update_actual_address(user_id, 'Санкт-Петербург')
    await callback_query.answer()
    await callback_query.message.edit_text( "10. Место работы", reply_markup=get_employment_keyboard())

async def process_employment(callback_query: types.CallbackQuery, state: FSMContext):
    global result
    user_id = callback_query.from_user.id
    if callback_query.data == 'employment_ip':
        result[f"score_{user_id}"] += 50
        update_employment(user_id, "ИП")
    elif callback_query.data == 'employment_ul':
        result[f"score_{user_id}"] += 35
        update_employment(user_id, "ЮЛ")
    elif callback_query.data == 'employment_private_practice':
        result[f"score_{user_id}"] += 0
        update_employment(user_id, "Частная практика")
    await callback_query.message.edit_text( "11. Стаж на последнем месте работы (лет)", reply_markup=get_work_experience_keyboard())

async def process_work_experience(callback_query: types.CallbackQuery, state: FSMContext):
    global result
    user_id = callback_query.from_user.id
    if callback_query.data == 'work_experience_12+':
        result[f"score_{user_id}"] += 35
        update_work_experience(user_id, '3 месяца')
    elif callback_query.data == 'work_experience_3-12':
        result[f"score_{user_id}"] += 15
        update_work_experience(user_id, 'от 3 до 1 года')
    elif callback_query.data == 'work_experience_more_-3':
        result[f"score_{user_id}"] += 0
        update_work_experience(user_id, 'Больше 1 года')
    await callback_query.message.edit_text("12. Частота смены работы за последние 5 лет", reply_markup=get_job_changes_keyboard())

async def process_job_changes(callback_query: types.CallbackQuery, state: FSMContext):
    global result
    user_id = callback_query.from_user.id
    if callback_query.data == 'job_changes_less_3':
        result[f"score_{user_id}"] += 35
        update_job_changes(user_id, "Не более трех")
    elif callback_query.data == 'job_changes_3_4':
        result[f"score_{user_id}"] += 25
        update_job_changes(user_id, "От трех до четырех")
    elif callback_query.data == 'job_changes_more_4':
        result[f"score_{user_id}"] += 5
        update_job_changes(user_id, "Более четырех")
    await callback_query.answer()
    await callback_query.message.edit_text( "13. Наличие карьерного роста за последние 5 лет", reply_markup=get_career_growth_keyboard())

async def process_career_growth(callback_query: types.CallbackQuery, state: FSMContext):
    global result
    user_id = callback_query.from_user.id
    if callback_query.data == 'career_growth_yes':
        result[f"score_{user_id}"] += 35
        update_career_growth(user_id, 'Есть')
    elif callback_query.data == 'career_growth_no':
        result[f"score_{user_id}"] += 25
        update_career_growth(user_id, 'Нет')
    await callback_query.answer()
    await callback_query.message.edit_text( "14. Заработная плата", reply_markup=get_salary_keyboard())

async def process_salary(callback_query: types.CallbackQuery, state: FSMContext):
    global result
    user_id = callback_query.from_user.id

    if callback_query.data == 'salary_more_50000':
        result[f"score_{user_id}"] += 35
        update_salary(user_id, "Больше 50000")
    elif callback_query.data == 'salary_30000_50000':
        result[f"score_{user_id}"] += 25
        update_salary(user_id, "Между 30000 и 50000")
    elif callback_query.data == 'salary_less_30000':
        result[f"score_{user_id}"] += 15
        update_salary(user_id, "Меньше 30000")
    await callback_query.message.edit_text("15. Документы, подтверждающие доход", reply_markup=get_income_documents_keyboard())

async def process_income_documents(callback_query: types.CallbackQuery, state: FSMContext):
    global result
    user_id = callback_query.from_user.id
    if callback_query.data == 'income_documents_salary_card':
        result[f"score_{user_id}"] += 35
        update_income_documents(user_id, "Зарплатная карта")
    elif callback_query.data == 'income_documents_2ndfl':
        result[f"score_{user_id}"] += 35
        update_income_documents(user_id, "Справка 2НДФЛ")
    elif callback_query.data == 'income_documents_free_form':
        result[f"score_{user_id}"] += 20
        update_income_documents(user_id, "Справка в свободной форме")
    elif callback_query.data == 'income_documents_no_document':
        result[f"score_{user_id}"] += 0
        update_income_documents(user_id, "Нет документа")
    await callback_query.answer()
    await callback_query.message.edit_text( "16. Другие источники дохода", reply_markup=get_other_income_keyboard())

async def process_other_income(callback_query: types.CallbackQuery, state: FSMContext):
    global result
    user_id = callback_query.from_user.id
    if callback_query.data.endswith('pension'):
        update_other_income(user_id, 'Пенсия')
    elif callback_query.data.endswith('interest_on_deposits'):
        update_other_income(user_id, 'Процент по вкладам')
    elif callback_query.data.endswith('rent'):
        update_other_income(user_id, 'Аренда')
    elif callback_query.data.endswith('alimony'):
        update_other_income(user_id, 'Алименты')
    elif callback_query.data.endswith('stipend'):
        update_other_income(user_id, 'Стипендия')
    elif callback_query.data.endswith('other'):
        update_other_income(user_id, 'Прочее')
    elif callback_query.data.endswith('no'):
        update_other_income(user_id, 'Нет')
    if callback_query.data.endswith('no'):
        await callback_query.message.edit_text("17. Расходы", reply_markup=get_expenses_keyboard())
    else:
        await callback_query.message.edit_text("Сумма доходов")
        await state.set_state(Form.doxod)

async def process_doxod(message: types.Message , state: FSMContext):
    global result
    user_id = message.from_user.id
    update_doxod(user_id, message.text)
    await message.answer("17. Расходы", reply_markup=get_expenses_keyboard())
    await state.clear()
    

async def process_expenses(callback_query: types.CallbackQuery, state: FSMContext):
    global result
    user_id = callback_query.from_user.id
    if callback_query.data.endswith('pension'):
        update_expenses(user_id, 'Расходы на обслуживание действующих кредитов')
    elif callback_query.data.endswith('interest_on_deposits'):
        update_expenses(user_id, 'Аренда имущества')
    elif callback_query.data.endswith('alimony'):
        update_expenses(user_id, 'Алименты')
    elif callback_query.data.endswith('utilities'):
        update_expenses(user_id, 'Коммунальные платежи')
    elif callback_query.data.endswith('other'):
        update_expenses(user_id, 'Прочее')
    elif callback_query.data.endswith('no'):
        update_other_income(user_id, 'Нет')
    if callback_query.data.endswith('no'):
        await callback_query.message.edit_text("18. Являетесь ли клиентом банка", reply_markup=get_bank_client_keyboard())
    else:
        await callback_query.message.edit_text("Сумма расходов")
        await state.set_state(Form.rashod)
    
async def process_rashod(message: types.Message , state: FSMContext):
    global result
    user_id = message.from_user.id
    update_rashod(user_id, message.text)
    await message.answer("18. Являетесь ли клиентом банка", reply_markup=get_bank_client_keyboard())
    await state.clear()

async def process_bank_client(callback_query: types.CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id
    global result
    if callback_query.data == 'bank_client_yes':
        result[f"score_{user_id}"] = result[f"score_{user_id}"]- 35
        update_bank_client(user_id, "Да")
    elif callback_query.data == 'bank_client_no':
        update_bank_client(user_id, "Нет")
        result[f"score_{user_id}"] = result[f"score_{user_id}"] - 15
    await callback_query.answer()
    await callback_query.message.edit_text( "19. Есть ли счет в банке", reply_markup=get_bank_account_keyboard())

async def process_bank_account(callback_query: types.CallbackQuery, state: FSMContext):
    global result
    user_id = callback_query.from_user.id
    if callback_query.data == 'bank_account_yes':
        result[f"score_{user_id}"] += 35
        update_bank_account(user_id, "Да")
    elif callback_query.data == 'bank_account_no':
        result[f"score_{user_id}"] += 15
        update_bank_account(user_id, 'Нет')
    await callback_query.message.edit_text( "20. Есть ли кредит в банке", reply_markup=get_bank_credit_keyboard())

async def process_bank_credit(callback_query: types.CallbackQuery, state: FSMContext):
    global result
    user_id = callback_query.from_user.id
    if callback_query.data == 'bank_credit_yes':
        result[f"score_{user_id}"] += 10
        update_bank_credit(user_id, 'Да')
    elif callback_query.data == 'bank_credit_no':
        result[f"score_{user_id}"] += 35
        update_bank_credit(user_id, 'Нет')
    await callback_query.answer()
    if callback_query.data == 'bank_credit_yes':
        await callback_query.message.edit_text("21. Впишите остаток по кредиту")
        await state.set_state(Form.bank_credit_monthly_payment)
    if callback_query.data == 'bank_credit_no':
         await callback_query.message.edit_text("22. Есть ли непогашенные кредиты в других банках", reply_markup=get_other_credits_keyboard())

async def process_bank_credit_remainder(message: types.Message, state: FSMContext):
    global result
    user_id = message.from_user.id
    remainder = message.text
    update_bank_credit_remainder(user_id, remainder)
    await message.answer("Напишите ваш ежемесячный платеж по кредиту")
    await state.set_state(Form.bank_credit_term)

async def process_bank_credit_monthly_payment(message: types.Message, state: FSMContext):
    global result
    user_id = message.from_user.id
    monthly_payment = message.text
    update_bank_credit_monthly_payment(user_id, monthly_payment)
    await message.answer("На какой срок у вас кредит")
    await state.set_state(Form.property)

async def process_bank_credit_property(message: types.Message, state: FSMContext):
    global result
    user_id = message.from_user.id
    monthly_payment = message.text
    update_bank_credit_term(user_id, monthly_payment)
    await message.answer("24. Есть ли предоставленные поручительства", reply_markup=get_suretyships_keyboard())
    await state.clear()

async def process_other_credits(callback_query: types.CallbackQuery, state: FSMContext):
    global result
    user_id = callback_query.from_user.id
    if callback_query.data == 'other_credits_yes':
        result[f"score_{user_id}"] += 10
        update_other_credits(user_id, "Да")
    elif callback_query.data == 'other_credits_no':
        result[f"score_{user_id}"] += 35
        update_other_credits(user_id, "Нет")
    await callback_query.answer()
    if callback_query.data == 'other_credits_yes':
        await callback_query.message.edit_text("23. Впишите остаток по кредиту")
        await state.set_state(Form.bank_credit_monthly_payment)
    if callback_query.data == 'other_credits_no' or callback_query.data == 'other_credits_any1' or callback_query.data == 'other_credits_any' or callback_query.data == 'other_credits_any3':
        await callback_query.message.edit_text("24. Есть ли предоставленные поручительства", reply_markup=get_suretyships_keyboard())
# 23 func don;t work callback
        
async def process_suretyships(callback_query: types.CallbackQuery, state: FSMContext):
    global result
    user_id = callback_query.from_user.id
    if callback_query.data == 'suretyships_yes':
        result[f"score_{user_id}"] += 10
        update_suretyships(user_id, "Да")
    elif callback_query.data == 'suretyships_no':
        result[f"score_{user_id}"] += 35
        update_suretyships(user_id, "Нет")
    if callback_query.data == 'suretyships_yes':
        await callback_query.message.edit_text("25. Впишите остаток по поручительству")
        await state.set_state(Form.bank_credit_monthly_payment_)
    if callback_query.data == 'suretyships_no' or callback_query.data == 'suretyships_any1' or callback_query.data == 'suretyships_any' or callback_query.data == 'suretyships_any3':
        await callback_query.message.edit_text("26.Являетесь ли Вы инвалидом", reply_markup=get_invalid_keyboard())


async def process_suretyships_remainder(message: types.Message, state: FSMContext):
    global result
    user_id = message.from_user.id
    remainder = message.text
    update_suretyships_remainder(user_id, remainder)
    await message.answer("Напишите ваш ежемесячный платеж по поручительству")
    await state.set_state(Form.bank_credit_term_)

async def process_suretyships_monthly_payment(message: types.Message, state: FSMContext):
    global result
    user_id = message.from_user.id
    monthly_payment = message.text
    update_suretyships_monthly_payment(user_id, monthly_payment)
    await message.answer("На какой срок у вас поручительство")
    await state.set_state(Form.property_)

async def process_suretyships_property(message: types.Message, state: FSMContext):
    global result
    user_id = message.from_user.id
    monthly_payment = message.text
    update_suretyships_term(user_id, monthly_payment)
    await message.answer("26.Являетесь ли Вы инвалидом", reply_markup=get_invalid_keyboard())
    await state.clear()



async def process_invalid_yes(callback_query: types.CallbackQuery, state: FSMContext): # Функция вызывается если 25 есть
    global result
    user_id = callback_query.from_user.id
    if callback_query == 'suretyship_any1':
        update_suretyships_details(user_id, "Остаток")
    if callback_query == 'suretyship_any':
        update_suretyships_details(user_id, "Ежемесячный платеж")
    if callback_query == 'suretyship_any3':
        update_suretyships_details(user_id, "Срок")
    await callback_query.message.edit_text("26.Являетесь ли Вы инвалидом", reply_markup=get_invalid_keyboard())

async def process_invalid(callback_query: types.CallbackQuery, state: FSMContext):
    global result
    user_id = callback_query.from_user.id
    if callback_query.data == 'invalid_yes':
        update_disability(user_id, "Инвалид")
    elif callback_query.data == 'invalid_no':
        result[f"score_{user_id}"] += 35
        update_disability(user_id, "Не инвалид")
    await callback_query.answer()
    await callback_query.message.edit_text( "27.Ведется ли\велось ли против Вас судопроизводство\участвуете \nли Вы\участвовали в судебном процессе", reply_markup=get_ychastie_keyboard())

async def process_ychastie(callback_query: types.CallbackQuery, state: FSMContext):
    global result
    user_id = callback_query.from_user.id
    if callback_query.data == 'ychastie_yes':
        update_legal_proceedings(user_id, "Да")
    elif callback_query.data == 'ychastie_no':
        result[f"score_{user_id}"] += 35
        update_legal_proceedings(user_id, "Нет")
    await callback_query.answer()
    await callback_query.message.edit_text( "28.Имеются ли решения суда, которые Вы не исполнили", reply_markup=get_reshenie_keyboard())

async def process_reshenie(callback_query: types.CallbackQuery, state: FSMContext):
    global result
    user_id = callback_query.from_user.id
    if callback_query.data == 'reshenie_yes':
        update_legal_proceedings_details(user_id, "Да")
    elif callback_query.data == 'reshenie_no':
        result[f"score_{user_id}"] += 35
        update_legal_proceedings_details(user_id, "Нет")
    await callback_query.answer()
    #await callback_query.message.edit_text( "29.Сведения о собственности", reply_markup=get_terms1_keyboard())
    await callback_query.message.answer_poll(question="29.Сведения о собственности",
                              options=[
                                  "Квартира",
                                  "Дача",
                                  "Автомобиль",
                                  "Мотоцикл",
                                  "Другое",
                                  "Нет"],
                              allows_multiple_answers=True,
                              reply_markup=kb_())


@router.callback_query(F.data == "test1")
async def process_svedenia_home(callback_query: types.CallbackQuery, state: FSMContext, event_update: Update):
    global result
    user_id = callback_query.from_user.id
    tpm_list = event_update.callback_query.message.poll.options
    result1 = [i.text for i in tpm_list if i.voter_count == 1]
    result12 = [i.voter_count for i in tpm_list]
    if "Квартира" in result:
        result[f"score_{user_id}"] += 35
        update_property(user_id, ", ".join(result1))
    elif "Квартира" not in result:
        result[f"score_{user_id}"] += 35
        update_property(user_id, ", ".join(result1))
    
    await callback_query.answer()
    if 1 in result12:
        await state.set_state(Form._2)
        await callback_query.message.answer("30.Стоимость собственности", reply_markup=get_cost_keyboard())
    if 1 not in result12:
         await callback_query.message.answer("Вы не выбрали!")


# User input

async def process_cost_home(callback_query: types.CallbackQuery, state: FSMContext):
    ic()
    global result
    user_id = callback_query.from_user.id
    if callback_query.data == 'cost_1000000':
        result[f"score_{user_id}"] += 35
        update_property_value(user_id, "Больше 1000000")
    elif callback_query.data == 'cost_50000_1000000':
        result[f"score_{user_id}"] += 25
        update_property_value(user_id, "Между 50000 и 1000000")
    elif callback_query.data == 'cost_50000':
        result[f"score_{user_id}"] += 15
        update_property_value(user_id, "Меньше 50000")
    await callback_query.answer()
    await callback_query.message.answer( "31.Номер телефона", reply_markup=phone)
    await state.set_state(Form.phone_number)

async def process_telephone(message: types.Message , state: FSMContext):
    global result
    try: # Проверка на types.Contact, если просто сообщение то except
        phone = message.contact.phone_number
    except:
        phone = message.text
    user_id = message.from_user.id
    if phone:
        await message.answer( "32.Адрес электронной почты", reply_markup=types.ReplyKeyboardRemove())
        update_phone_number(user_id, phone)
        await state.set_state(Form.email)
    else:
        await message.answer( "Номер должен начинаться с +7!")
        await state.set_state(Form.phone_number)

async def process_email(message: types.Message , state: FSMContext):
    global result
    user_id = message.from_user.id
    if "@" in message.text:
        await message.answer( "33.Сумма кредита (число)")
        update_email(user_id, message.text)
        await state.set_state(Form.credit_amount)
    else:
        await message.answer( "Почта должна содержать @!")
        await state.set_state(Form.email)

async def process_credit_amount(message: types.Message , state: FSMContext):
    global result
    user_id = message.from_user.id
    try:
        update_credit_amount(user_id, int(message.text))
    except:
        update_test_amount(user_id, int(message.text))
    await message.answer( "34.Цель кредита", reply_markup=get_credit_purpose_keyboard())
    await state.set_state(Form.credit_purpose)

async def process_credit_purpose(message: types.Message , state: FSMContext):
    global result
    user_id = message.from_user.id
    update_credit_purpose(user_id, message.text)
    await message.answer( "35.На какой срок (месяц)", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(Form.credit_term)

async def process_credit_term(message: types.Message , state: FSMContext):
    global result
    user_id = message.from_user.id
    update_credit_term(user_id, message.text)
    await message.answer( "36.По какой процентной ставке (число)")
    await state.set_state(Form.credit_rate)

async def process_credit_rate(message: types.Message , state: FSMContext):
    await state.clear()
    global result
    user_id = message.from_user.id
    update_credit_rate(user_id, message.text)
    update_result(user_id, result[f"score_{user_id}"])
    message.answer(f"Ваш результат - {result[f'score_{user_id}']} баллов.")
    if  690 < result[f"score_{user_id}"] < 850:
        await message.answer( "690-850 баллов – клиент с высокой платежеспособностью, на хорошем счету в банке, поэтому может получить крупную сумму займа на выгодных условиях.")
    if  650 < result[f"score_{user_id}"] < 690:
        await message.answer( "650-690 баллов – хорошая кредитоспособность. Клиент получит кредит на стандартных условиях. Сумма уточняется на собеседовании с сотрудниками банка.")
    if  600 < result[f"score_{user_id}"] < 650:
        await message.answer( "600-650 баллов – средняя кредитоспособность. Обычно таким клиентам выдают заем, но на достаточно жестких условиях. Банк ставит ограничения по срокам, сумме кредита.")
    if  500 < result[f"score_{user_id}"] < 600:
        await message.answer( "500-600 баллов – низкая кредитоспособность. Клиент всё ещё может получить заем, но небольшой и под высокий процент.")
    if  300 < result[f"score_{user_id}"] < 500:
        await message.answer( "300-500 баллов – неблагонадежный клиент. Банк кредит не выдаст.")
    await message.answer("Ожидайте, идёт расчёт кредита!")
    amount = sql.execute(f"Select * from people where id = ({user_id})")
    loan_amount:int = amount.fetchone()[40] # на какую сумму
    term = sql.execute(f"Select * from people where id = ({user_id})")
    loan_term_years:int = term.fetchone()[42] # на сколько месяцев
    annual_interest_rate:int = worksheet.acell('AS2').value # берем ставку из таблицы
    print(annual_interest_rate)
    monthly_interest_rate:float = int(annual_interest_rate) / 100 / 12 # Преобразование годовой ставки в месячную
    annuity_coefficient:float = calculate_annuity_coefficient(float(monthly_interest_rate), int(loan_term_years)) # Расчет коэффициента аннуитета
    monthly_payment:float = calculate_monthly_payment(int(loan_amount), float(annuity_coefficient))   # Расчет ежемесячного платежа
    payment:float = calculate_differentiated_payment(int(loan_amount), float(monthly_interest_rate), int(loan_term_years), 1)
    #await message.answer(f"Аннуитетный платёж: {monthly_payment:.2f} ₽\nДифференцированный платеж: {payment:.2f} ₽")
    dolg = loan_amount/loan_term_years
    procent = int(annual_interest_rate) / 100
    link = await create_sheet_for_user(loan_term_years,loan_amount,dolg,procent,monthly_payment)
    await message.answer(f"По предварительным подсчетам лимит кредита составляет {ran(loan_amount)} рублей с процентной ставкой {annual_interest_rate}%\nЕжемесячный платеж в течениe {loan_term_years} месяцев составит: Аннуитетный платёж: {monthly_payment:.2f} ₽\nДифференцированный платеж: {payment:.2f} ₽\nСсылка на таблицу с расчетом, с дифференцированными платежами и с аннуитетными платежами.\n{link}")
    
    update_payment1(user_id, f"{monthly_payment:.2f}") #Добаления в дб Аннуитетный платежа
    update_payment2(user_id, f"{payment:.2f}") #Добаления в дб Дифференцированный платежа
    
    try: #Добавления в таблицу всех результатов опроса
        data_of_user = normal_user_row(user_id)
        worksheet.update(f"B{db_[f'row_{user_id}']}:AS{db_[f'row_{user_id}']}", [data_of_user])
    except: ...
    