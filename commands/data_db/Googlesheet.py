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

#my_list = [
#    'id', 'пол', 'возраст', 'семейное положение', 'брачный контракт',
#    'члены семьи', 'доход супруга', 'образование','доход','расходы', 'адрес регистрации',
#    'фактический адрес', 'место работы', 'опыт работы', 'смена работы',
#    'карьерный_рост', 'зарплата', 'документы о доходах', 'другие доходы',
#    'расходы', 'клиент банка', 'банковский счёт', 'банковский кредит',
#    'реквизиты банковского кредита', 'другие кредиты',
#    'реквизиты других кредитов', 'поручительства','остаток по кредиту','ежемесячный платеж по кредиту','срок кредита', 'инвалидность',
#    'судебные разбирательства', 'детали судебного разбирательства',
#    'имущество', 'стоимость имущества', 'номер телефона',
#    'электронная почта', 'сумма кредита', 'цель кредита', 'срок кредита',
#    'кредитная ставка', 'результат',"аннуитетный платёж","дифференцированный платеж",'Ставка'
#]
#print(len(my_list))
#worksheet.update('A1:AS1', [my_list])