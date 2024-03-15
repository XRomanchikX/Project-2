from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, ReplyKeyboardBuilder, KeyboardButton

def get_admin_panel_keyboard():
   keyboard = InlineKeyboardBuilder()
   keyboard.add(InlineKeyboardButton(text='Ставка', callback_data='admin_stavka'))
   keyboard.add(InlineKeyboardButton(text='Результаты', callback_data='admin_result'))
   return keyboard.as_markup()

def get_result_keyboard():
   keyboard = InlineKeyboardBuilder()
   keyboard.add(InlineKeyboardButton(text='Посмотреть результаты', url="https://docs.google.com/spreadsheets/d/1nB8jtKhYRqSY51cT9ZU0fAQkKshGq8hGkrSXUKZvUy0/edit?usp=sharing"))
   keyboard.add(InlineKeyboardButton(text='Назад', callback_data='admin_back'))
   return keyboard.as_markup()

def get_stavka_keyboard():
   keyboard = InlineKeyboardBuilder()
   keyboard.add(InlineKeyboardButton(text='Да', callback_data='admin_stavka_edit'),
                (InlineKeyboardButton(text='Отмена', callback_data='admin_back')))
   return keyboard.as_markup()

def get_cancel_edit_keyboard():
   keyboard = InlineKeyboardBuilder()
   keyboard.add(InlineKeyboardButton(text='Отмена', callback_data='admin_back'))
   return keyboard.as_markup()


