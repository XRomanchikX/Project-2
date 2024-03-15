import logging
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
import secret.settings as settings
from handler import *
from admin_commands.adminpanel import *

async def start():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s")
    bot = Bot(token=settings.TOKEN, parse_mode='HTML')
    dp = Dispatcher()

    # main commands
    #dp.callback_query.register(start_call,F.data == "test")
    #dp.message.register(start_mess, Command(commands=['test']))
    
    dp.message.register(start_command, Command(commands=['start']))
    dp.callback_query.register(start_questions,F.data == "questions_start") # _1
    dp.callback_query.register(process_gender,F.data.startswith("gender_")) # _2
    dp.callback_query.register(process_age,F.data.startswith("age_")) # _3
    dp.callback_query.register(process_marital_status,F.data.startswith("marital_")) # _4
    dp.callback_query.register(process_marriage_contract,F.data.startswith("marriage_")) # _5
    dp.callback_query.register(process_family_member,F.data.startswith("family_")) # _6
    dp.callback_query.register(process_spouse_income,F.data.startswith("spouse_")) # _7
    dp.callback_query.register(process_education,F.data.startswith("education_")) # _8
    dp.callback_query.register(process_registration_address,F.data.startswith("registration_address_")) # _9
    dp.callback_query.register(process_actual_address,F.data.startswith("actual_address_")) # _10
    dp.callback_query.register(process_employment,F.data.startswith("employment_")) # _11
    dp.callback_query.register(process_work_experience,F.data.startswith("work_experience_")) # _12
    dp.callback_query.register(process_job_changes,F.data.startswith("job_changes_")) # _13
    dp.callback_query.register(process_career_growth,F.data.startswith("career_growth_")) # _14
    dp.callback_query.register(process_salary,F.data.startswith("salary_")) # _15
    dp.callback_query.register(process_income_documents,F.data.startswith("income_documents_")) # _16
    dp.callback_query.register(process_other_income,F.data.startswith("other_income_")) # _17
    dp.callback_query.register(process_expenses,F.data.startswith("expenses_")) # _18
    dp.message.register(process_rashod, Form.rashod)  # _32
    dp.message.register(process_doxod, Form.doxod)
    dp.callback_query.register(process_bank_client,F.data.startswith("bank_client_")) # _19
    dp.message.register(process_bank_credit_remainder, Form.bank_credit_monthly_payment)
    dp.message.register(process_bank_credit_monthly_payment, Form.bank_credit_term)
    dp.message.register(process_bank_credit_property, Form.property)
    dp.callback_query.register(process_bank_account,F.data.startswith("bank_account_")) # _20
    dp.callback_query.register(process_bank_credit,F.data.startswith("bank_credit_")) # _21
    dp.callback_query.register(process_other_credits,F.data.startswith("other_credits_")) # _22
    dp.callback_query.register(process_suretyships,F.data.startswith("suretyships_")) # _23
    dp.message.register(process_suretyships_remainder, Form.bank_credit_monthly_payment_)
    dp.message.register(process_suretyships_monthly_payment, Form.bank_credit_term_)
    dp.message.register(process_suretyships_property, Form.property_)
    dp.callback_query.register(process_invalid,F.data.startswith("invalid_")) # _24
    dp.callback_query.register(process_invalid_yes,F.data.startswith("suretyship_")) # _25
    dp.callback_query.register(process_ychastie,F.data.startswith("ychastie_")) # _26
    dp.callback_query.register(process_reshenie,F.data.startswith("reshenie_")) # _27
    dp.callback_query.register(process_svedenia_home,F.data == "test1")

    dp.callback_query.register(process_cost_home, F.data.startswith("cost_")) # _29
    dp.message.register(process_telephone, Form.phone_number) # _30
    dp.message.register(process_email, Form.email)  # _31
    dp.message.register(process_credit_amount, Form.credit_amount)  # _32
    dp.message.register(process_credit_purpose, Form.credit_purpose)  # _33
    dp.message.register(process_credit_term, Form.credit_term)  # _34
    dp.message.register(process_credit_rate, Form.credit_rate)  # _35

    # admin panel
    dp.message.register(admin_panel, Command(commands=['admin']))
    dp.callback_query.register(admin_result, F.data == "admin_result")
    dp.callback_query.register(admin_stavka, F.data == "admin_stavka")
    dp.callback_query.register(admin_stavka_edit, F.data == "admin_stavka_edit")
    dp.callback_query.register(admin_panel_call, F.data == "admin_back")
    dp.message.register(admin_new_stavka, FormAdmin.edit_stavka)


    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(start())