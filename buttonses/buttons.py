from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, ReplyKeyboardBuilder, KeyboardButton, ReplyKeyboardMarkup

def get_start_keyboard():
   keyboard = InlineKeyboardBuilder()
   keyboard.add(InlineKeyboardButton(text='Рассчитать кредит', callback_data='questions_start'))
   keyboard.adjust(1)
   return keyboard.as_markup()

def get_gender_keyboard():
   keyboard = InlineKeyboardBuilder()
   keyboard.add(InlineKeyboardButton(text='Мужской', callback_data='gender_male'))
   keyboard.add(InlineKeyboardButton(text='Женский', callback_data='gender_female'))
   keyboard.adjust(1)
   return keyboard.as_markup()

def get_age_keyboard():
   keyboard = InlineKeyboardBuilder()
   keyboard.add(InlineKeyboardButton(text='Менее 23 лет', callback_data='age_less_23'))
   keyboard.add(InlineKeyboardButton(text='От 25 до 45 лет', callback_data='age_25_45'))
   keyboard.add(InlineKeyboardButton(text='От 46 до 55 лет', callback_data='age_46_55'))
   keyboard.add(InlineKeyboardButton(text='Более 56 лет', callback_data='age_more_56'))
   keyboard.adjust(1)
   return keyboard.as_markup()

def get_marital_status_keyboard():
   keyboard = InlineKeyboardBuilder()
   keyboard.add(InlineKeyboardButton(text='Женат/Замужем', callback_data='marital_married'))
   keyboard.add(InlineKeyboardButton(text='Разведен(а)', callback_data='marital_divorced'))
   keyboard.add(InlineKeyboardButton(text='Холост(не замужем)', callback_data='marital_single'))
   keyboard.add(InlineKeyboardButton(text='Вдовец(вдова)', callback_data='marital_widowed'))
   keyboard.adjust(1)
   return keyboard.as_markup()

def get_marriage_contract_keyboard():
   keyboard = InlineKeyboardBuilder()
   keyboard.add(InlineKeyboardButton(text='Да', callback_data='marriage_yes'))
   keyboard.add(InlineKeyboardButton(text='Нет', callback_data='marriage_no'))
   keyboard.adjust(1)
   return keyboard.as_markup()

def get_family_members_keyboard():
   keyboard = InlineKeyboardBuilder()
   keyboard.add(InlineKeyboardButton(text='1', callback_data='family_mother'))
   keyboard.add(InlineKeyboardButton(text='2', callback_data='family_father'))
   keyboard.add(InlineKeyboardButton(text='3', callback_data='family_brother'))
   keyboard.add(InlineKeyboardButton(text='4', callback_data='family_sister'))
   keyboard.add(InlineKeyboardButton(text='5', callback_data='family_spouse'))
   keyboard.adjust(1)
   return keyboard.as_markup()

def get_spouse_keyboard():
   keyboard = InlineKeyboardBuilder()
   keyboard.add(InlineKeyboardButton(text='> 50000', callback_data='spouse_income_more_50000'))
   keyboard.add(InlineKeyboardButton(text='30000 - 50000', callback_data='spouse_income_30000_50000'))
   keyboard.add(InlineKeyboardButton(text='< 30000', callback_data='spouse_income_less_30000'))
   keyboard.adjust(1)
   return keyboard.as_markup()

def get_education_keyboard():
   keyboard = InlineKeyboardBuilder()
   keyboard.add(InlineKeyboardButton(text='Ученая степень, 2 и более высших образований', callback_data='education_high'))
   keyboard.add(InlineKeyboardButton(text='Высшее', callback_data='education_higher'))
   keyboard.add(InlineKeyboardButton(text='Незаконченное высшее', callback_data='education_incomplete'))
   keyboard.add(InlineKeyboardButton(text='Средне-специальное', callback_data='education_secondary_special'))
   keyboard.add(InlineKeyboardButton(text='Среднее', callback_data='education_secondary'))
   keyboard.adjust(1)
   return keyboard.as_markup()

def get_registration_address_keyboard():
    keyboard = InlineKeyboardBuilder()  
    keyboard.add(InlineKeyboardButton(text='Нет', callback_data='registration_address_no'))
    keyboard.add(InlineKeyboardButton(text='Есть', callback_data='registration_address_yes'))
    keyboard.adjust(1)
    return keyboard.as_markup()

def get_actual_address_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Село, деревня', callback_data='actual_address_village'))
    keyboard.add(InlineKeyboardButton(text='Город', callback_data='actual_address_city'))
    keyboard.add(InlineKeyboardButton(text='Москва', callback_data='actual_address_moscow'))
    keyboard.add(InlineKeyboardButton(text='Санкт-Петербург', callback_data='actual_address_spb'))
    keyboard.adjust(1)
    return keyboard.as_markup()

def get_employment_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='ИП', callback_data='employment_ip'))
    keyboard.add(InlineKeyboardButton(text='ЮЛ', callback_data='employment_ul'))
    keyboard.add(InlineKeyboardButton(text='Частная практика', callback_data='employment_private_practice'))
    keyboard.adjust(1)
    return keyboard.as_markup()

def get_work_experience_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='3 месяца', callback_data='work_experience_more_-3'))
    keyboard.add(InlineKeyboardButton(text='от 3 до 1 года', callback_data='work_experience_3-12'))
    keyboard.add(InlineKeyboardButton(text='Больше 1 года', callback_data='work_experience_12+'))
    keyboard.adjust(1)
    return keyboard.as_markup()

def get_job_changes_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Не более трех', callback_data='job_changes_less_3'))
    keyboard.add(InlineKeyboardButton(text='От трех до четырех', callback_data='job_changes_3_4'))
    keyboard.add(InlineKeyboardButton(text='Более четырех', callback_data='job_changes_more_4'))
    keyboard.adjust(1)
    return keyboard.as_markup()

def get_career_growth_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Есть', callback_data='career_growth_yes'))
    keyboard.add(InlineKeyboardButton(text='Нет', callback_data='career_growth_no'))
    keyboard.adjust(1)
    return keyboard.as_markup()

def get_salary_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='> 50000', callback_data='salary_more_50000'))
    keyboard.add(InlineKeyboardButton(text='30000 - 50000', callback_data='salary_30000_50000'))
    keyboard.add(InlineKeyboardButton(text='< 30000', callback_data='salary_less_30000'))
    keyboard.adjust(1)
    return keyboard.as_markup()

def get_income_documents_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Зарплатная карта', callback_data='income_documents_salary_card'))
    keyboard.add(InlineKeyboardButton(text='Справка 2НДФЛ', callback_data='income_documents_2ndfl'))
    keyboard.add(InlineKeyboardButton(text='Справка в свободной форме', callback_data='income_documents_free_form'))
    keyboard.add(InlineKeyboardButton(text='Нет документа', callback_data='income_documents_no_document'))
    keyboard.adjust(1)
    return keyboard.as_markup()

def get_other_income_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Пенсия', callback_data='other_income_pension'))
    keyboard.add(InlineKeyboardButton(text='Процент по вкладам', callback_data='other_income_interest_on_deposits'))
    keyboard.add(InlineKeyboardButton(text='Аренда', callback_data='other_income_rent'))
    keyboard.add(InlineKeyboardButton(text='Алименты', callback_data='other_income_alimony'))
    keyboard.add(InlineKeyboardButton(text='Стипендия', callback_data='other_income_stipend'))
    keyboard.add(InlineKeyboardButton(text='Прочее', callback_data='other_income_other'))
    keyboard.add(InlineKeyboardButton(text='Нет', callback_data='other_income_no'))
    keyboard.adjust(1)
    return keyboard.as_markup()

def get_expenses_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Расходы на обслуживание действующих кредитов', callback_data='expenses_pension'))
    keyboard.add(InlineKeyboardButton(text='Аренда имущества', callback_data='expenses_interest_on_deposits'))
    keyboard.add(InlineKeyboardButton(text='Алименты', callback_data='expenses_rent'))
    keyboard.add(InlineKeyboardButton(text='Коммунальные платежи', callback_data='expenses_alimony'))
    keyboard.add(InlineKeyboardButton(text='Прочее', callback_data='expenses_other'))
    keyboard.add(InlineKeyboardButton(text='Нет', callback_data='expenses_no'))
    keyboard.adjust(1)
    return keyboard.as_markup()

def get_bank_client_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Да', callback_data='bank_client_yes'))
    keyboard.add(InlineKeyboardButton(text='Нет', callback_data='bank_client_no'))
    keyboard.adjust(1)
    return keyboard.as_markup()

def get_bank_account_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Да', callback_data='bank_account_yes'))
    keyboard.add(InlineKeyboardButton(text='Нет', callback_data='bank_account_no'))
    keyboard.adjust(1)
    return keyboard.as_markup()

def get_bank_credit_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Да', callback_data='bank_credit_yes'))
    keyboard.add(InlineKeyboardButton(text='Нет', callback_data='bank_credit_no'))
    keyboard.adjust(1)
    return keyboard.as_markup()

def get_bank_credit_details_our_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Далее', callback_data='other_credits_no'))
    keyboard.adjust(1)
    return keyboard.as_markup()

def get_bank_credit_details_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Остаток', callback_data='suretyships_any1'))
    keyboard.add(InlineKeyboardButton(text='Ежемесячный платеж', callback_data='suretyships_any'))
    keyboard.add(InlineKeyboardButton(text='Срок', callback_data='suretyships_any3'))
    keyboard.adjust(1)
    return keyboard.as_markup()

def get_other_credits_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Да', callback_data='other_credits_yes'))
    keyboard.add(InlineKeyboardButton(text='Нет', callback_data='other_credits_no'))
    keyboard.adjust(1)
    return keyboard.as_markup()

def get_suretyships_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Да', callback_data='suretyships_yes'))
    keyboard.add(InlineKeyboardButton(text='Нет', callback_data='suretyships_no'))
    keyboard.adjust(1)
    return keyboard.as_markup()

def get_invalid_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Да', callback_data='invalid_yes'))
    keyboard.add(InlineKeyboardButton(text='Нет', callback_data='invalid_no'))
    keyboard.adjust(1)
    return keyboard.as_markup()

def get_invalid2_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Остаток', callback_data='suretyship_any1'))
    keyboard.add(InlineKeyboardButton(text='Ежемесячный платеж', callback_data='suretyship_any'))
    keyboard.add(InlineKeyboardButton(text='Срок', callback_data='suretyship_any3'))
    keyboard.adjust(1)
    return keyboard.as_markup()

def get_ychastie_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Да', callback_data='ychastie_yes'))
    keyboard.add(InlineKeyboardButton(text='Нет', callback_data='ychastie_no'))
    keyboard.adjust(1)
    return keyboard.as_markup()

def get_reshenie_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Да', callback_data='reshenie_yes'))
    keyboard.add(InlineKeyboardButton(text='Нет', callback_data='reshenie_no'))
    keyboard.adjust(1)
    return keyboard.as_markup()

def get_terms1_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Квартира', callback_data='terms_kv'))
    keyboard.add(InlineKeyboardButton(text='Дача', callback_data='terms_any1'))
    keyboard.add(InlineKeyboardButton(text='Автомобиль', callback_data='terms_any2'))
    keyboard.add(InlineKeyboardButton(text='Мотоцикл', callback_data='terms_any3'))
    keyboard.add(InlineKeyboardButton(text='Другое', callback_data='terms_any4'))
    keyboard.add(InlineKeyboardButton(text='Нет', callback_data='terms_no'))
    keyboard.adjust(1)
    return keyboard.as_markup()

def get_cost_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='> 1000000', callback_data='cost_1000000'))
    keyboard.add(InlineKeyboardButton(text='50000 - 1000000', callback_data='cost_50000_1000000'))
    keyboard.add(InlineKeyboardButton(text='< 50000', callback_data='cost_50000'))
    keyboard.adjust(1)
    return keyboard.as_markup()

phone=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить номер телефона",request_contact=True)
        ]
    ],
    resize_keyboard=True,
)


def get_svedenia_keyboard():
    keyboard1 = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text='Деньги на любые цели')
        ],
        [
            KeyboardButton(text='Рефинансирование кредита')
        ],
        [
            KeyboardButton(text='Приобретение недвижимости')
        ],
        [
            KeyboardButton(text='Покупка автомобиля')
        ],
        [
            KeyboardButton(text='Ипотека')
        ],
        [
            KeyboardButton(text='Рефинансирование ипотеки')
        ]
    ],resize_keyboard=True)
    return keyboard1

def get_credit_purpose_keyboard():
    keyboard1 = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text='Деньги на любые цели')
        ],
        [
            KeyboardButton(text='Рефинансирование кредита')
        ],
        [
            KeyboardButton(text='Приобретение недвижимости')
        ],
        [
            KeyboardButton(text='Покупка автомобиля')
        ],
        [
            KeyboardButton(text='Ипотека')
        ],
        [
            KeyboardButton(text='Рефинансирование ипотеки')
        ]
    ],resize_keyboard=True)
    return keyboard1

def kb_():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Далее', callback_data='test1'))
    keyboard.adjust(1)
    return keyboard.as_markup()

def kb_1():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Далее', callback_data='test'))
    keyboard.adjust(1)
    return keyboard.as_markup()