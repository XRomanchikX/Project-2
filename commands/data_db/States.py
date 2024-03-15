from aiogram.fsm.state import StatesGroup, State

class Form(StatesGroup):
    property_value = State()
    phone_number = State()
    email = State()
    credit_amount = State()
    credit_purpose = State()
    credit_term = State()
    credit_rate = State()
    bank_credit_monthly_payment = State()
    bank_credit_term = State()
    property = State()
    rashod = State()
    doxod = State()
    bank_credit_monthly_payment_ = State()
    bank_credit_term_ = State()
    property_ = State()


    _1 = State()
    _2 = State()
    _3 = State()

class FormAdmin(StatesGroup):
    edit_stavka = State()

import random
def ran(c1):
    c2 = random.randint(25000, 675000)
    res = c1+c2
    return res