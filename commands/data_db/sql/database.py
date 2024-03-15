import sqlite3 #db

db = sqlite3.connect('result.db');sql = db.cursor() # db_connect

sql.execute("""CREATE TABLE IF NOT EXISTS people (
   id TEXT,
   gender TEXT,
   age TEXT,
   marital_status TEXT,
   marriage_contract TEXT,
   family_members TEXT,
   spouse_income TEXT,
   education TEXT,
   doxod TEXT,
   rashod TEXT,
   registration_address TEXT,
   actual_address TEXT,
   employment TEXT,
   work_experience TEXT,
   job_changes TEXT,
   career_growth TEXT,
   salary TEXT,
   income_documents TEXT,
   other_income TEXT,
   expenses TEXT,
   bank_client TEXT,
   bank_account TEXT,
   bank_credit TEXT,
   bank_credit_details TEXT,
   bank_credit_term TEXT,
   bank_credit_monthly_payment TEXT,
   bank_credit_remainder TEXT,
   other_credits TEXT,
   other_credits_details TEXT,
   suretyships TEXT,
   suretyships_term TEXT,
   suretyships_monthly_payment TEXT,
   suretyships_remainder TEXT,
   disability TEXT,
   legal_proceedings TEXT,
   legal_proceedings_details TEXT,
   property TEXT,
   property_value TEXT,
   phone_number TEXT,
   email TEXT,
   credit_amount INT,
   credit_purpose TEXT,
   credit_term INT,
   credit_rate TEXT,
   result TEXT,
   annuity_payment TEXT,
   differentiated_payment TEXT
);""")
db.commit() #Create_db

# Function to insert a new person into the people table
def insert_person(data):
    sql.execute('''
        INSERT INTO people VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', data)
    db.commit()

# Function to retrieve data for a specific user by user_id
def get_person_by_id(user_id):
    sql.execute('SELECT * FROM people WHERE id = ?', (user_id))
    return sql.fetchone()

def insert_user_id(user_id):
    conn = sqlite3.connect('result.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO people (id) VALUES (?)', (user_id,))
    conn.commit()
    conn.close()

