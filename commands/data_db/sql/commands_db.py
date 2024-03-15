import sqlite3

db = sqlite3.connect('result.db');sql = db.cursor() # db_connect

def update_gender(user_id, value):
    sql.execute(f"UPDATE people SET gender = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_age(user_id, value):
    sql.execute(f"UPDATE people SET age = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_marital_status(user_id, value):
    sql.execute(f"UPDATE people SET marital_status = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_marriage_contract(user_id, value):
    sql.execute(f"UPDATE people SET marriage_contract = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_family_members(user_id, value):
    sql.execute(f"UPDATE people SET family_members = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_spouse_income(user_id, value):
    sql.execute(f"UPDATE people SET spouse_income = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_education(user_id, value):
    sql.execute(f"UPDATE people SET education = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_registration_address(user_id, value):
    sql.execute(f"UPDATE people SET registration_address = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_actual_address(user_id, value):
    sql.execute(f"UPDATE people SET actual_address = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_employment(user_id, value):
    sql.execute(f"UPDATE people SET employment = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_work_place(user_id, value):
    sql.execute(f"UPDATE people SET work_place = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_work_experience(user_id, value):
    sql.execute(f"UPDATE people SET work_experience = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_job_changes(user_id, value):
    sql.execute(f"UPDATE people SET job_changes = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_career_growth(user_id, value):
    sql.execute(f"UPDATE people SET career_growth = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_salary(user_id, value):
    sql.execute(f"UPDATE people SET salary = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_income_documents(user_id, value):
    sql.execute(f"UPDATE people SET income_documents = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_other_income(user_id, value):
    sql.execute(f"UPDATE people SET other_income = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_expenses(user_id, value):
    sql.execute(f"UPDATE people SET expenses = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_bank_client(user_id, value):
    sql.execute(f"UPDATE people SET bank_client = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_bank_account(user_id, value):
    sql.execute(f"UPDATE people SET bank_account = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_bank_credit(user_id, value):
    sql.execute(f"UPDATE people SET bank_credit = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_bank_credit_details(user_id, value):
    sql.execute(f"UPDATE people SET bank_credit_details = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_other_credits(user_id, value):
    sql.execute(f"UPDATE people SET other_credits = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_other_credits_details(user_id, value):
    sql.execute(f"UPDATE people SET other_credits_details = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_suretyships(user_id, value):
    sql.execute(f"UPDATE people SET suretyships = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_suretyships_details(user_id, value):
    sql.execute(f"UPDATE people SET suretyships_details = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_disability(user_id, value):
    sql.execute(f"UPDATE people SET disability = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_legal_proceedings(user_id, value):
    sql.execute(f"UPDATE people SET legal_proceedings = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_legal_proceedings_details(user_id, value):
    sql.execute(f"UPDATE people SET legal_proceedings_details = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_property(user_id, value):
    sql.execute(f"UPDATE people SET property = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_property_value(user_id, value):
    sql.execute(f"UPDATE people SET property_value = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_phone_number(user_id, value):
    sql.execute(f"UPDATE people SET phone_number = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_email(user_id, value):
    sql.execute(f"UPDATE people SET email = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_credit_amount(user_id, value):
    sql.execute(f"UPDATE people SET credit_amount = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_credit_purpose(user_id, value):
    sql.execute(f"UPDATE people SET credit_purpose = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_credit_term(user_id, value):
    sql.execute(f"UPDATE people SET credit_term = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_credit_rate(user_id, value):
    sql.execute(f"UPDATE people SET credit_rate = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_result(user_id, value):
    sql.execute(f"UPDATE people SET result = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_payment1(user_id, value):
    sql.execute(f"UPDATE people SET annuity_payment = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_payment2(user_id, value):
    sql.execute(f"UPDATE people SET differentiated_payment = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_test_amount(user_id, value):
    sql.execute(f"UPDATE people SET differentiated_payment = ? WHERE id = ?", (value, user_id))
    db.commit()



def update_bank_credit_remainder(user_id, value):
    sql.execute(f"UPDATE people SET bank_credit_remainder = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_bank_credit_monthly_payment(user_id, value):
    sql.execute(f"UPDATE people SET bank_credit_monthly_payment = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_bank_credit_term(user_id, value):
    sql.execute(f"UPDATE people SET bank_credit_term = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_rashod(user_id, value):
    sql.execute(f"UPDATE people SET rashod = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_doxod(user_id, value):
    sql.execute(f"UPDATE people SET doxod = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_suretyships_remainder(user_id, value):
    sql.execute(f"UPDATE people SET suretyships_remainder = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_suretyships_monthly_payment(user_id, value):
    sql.execute(f"UPDATE people SET suretyships_monthly_payment = ? WHERE id = ?", (value, user_id))
    db.commit()

def update_suretyships_term(user_id, value):
    sql.execute(f"UPDATE people SET suretyships_term = ? WHERE id = ?", (value, user_id))
    db.commit()

def get_user_data(user_id):
    query = "SELECT * FROM people WHERE id = ?"
    sql.execute(query, (user_id,))

    results = sql.fetchall()

    for row in results:
        return row