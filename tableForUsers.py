import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Устанавливаем область видимости (scope) и учетные данные для доступа к Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('your-credentials.json', scope)
client = gspread.authorize(creds)

# Создаем новый документ Google Sheets и возвращаем ссылку
async def create_sheet_for_user(mouth, ostatok, dolg, procent_const, sum_plateja):
    new_sheet = client.create("Сведения о кредите")
    worksheet = new_sheet.get_worksheet(0)

    # Вносим данные в таблицу
    headers = ["Номер Платежа", "Остаток платежа, ₽", "Проценты, ₽", "Основной долг, ₽", "Сумма платежа, ₽","|","Номер Платежа", "Остаток платежа, ₽", "Проценты, ₽", "Основной долг, ₽", "Сумма платежа, ₽"]
    worksheet.append_row(headers)
    ostatok1 = ostatok
    ostatock_const = ostatok

     #Создаем матрицу данных
    for i in range(0, int(mouth)):
        i+=1
        procent = ostatok * procent_const * 31 / 365
        dolg = sum_plateja - procent
        ostatok = ostatok - dolg

        procent1 = ostatok1 * procent_const * 31 / 365
        dolg1 = ostatock_const / mouth
        ostatok1 = ostatok1 - dolg1
        platej1 = dolg1 + procent1
        row = [f"{i}", f"{ostatok:.2f}", f"{procent:.2f}", f"{dolg:.2f}", f"{sum_plateja:.2f}", "|", f"{i}", f"{ostatok1:.2f}", f"{procent1:.2f}", f"{dolg1:.2f}", f"{platej1:.2f}"]
        worksheet.append_row(row)
        
    # Вносим матрицу в таблицу
    worksheet.append_row(['Итог','0',f'{round((sum_plateja*48)-ostatock_const)}',f'{ostatock_const}',f'{round((sum_plateja*48)):.2f}',"|",'Итог','0',f'{round((sum_plateja*48)-ostatock_const)}',f'{ostatock_const}',f'{round((sum_plateja*48)):.2f}'])
    #Закрываем доступ для публичного просмотра (по желанию)
    new_sheet.share("", perm_type="anyone", role="reader")

    # Возвращаем ссылку на созданный документ
    return new_sheet.url
    

user_names = ['1']