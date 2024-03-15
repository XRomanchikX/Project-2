def calculate_annuity_coefficient(monthly_interest_rate, loan_term):
    return (monthly_interest_rate * (1 + monthly_interest_rate) ** loan_term) / ((1 + monthly_interest_rate) ** loan_term - 1)

def calculate_monthly_payment(loan_amount, annuity_coefficient):
    return loan_amount * annuity_coefficient



#print(f"Коэффициент аннуитета: {annuity_coefficient:.5f}")
#print(f"Ежемесячный платеж: {monthly_payment:.2f} ₽")


def calculate_differentiated_payment(loan_amount, monthly_interest_rate, loan_term_months, month):
    differentiated_payment = loan_amount / loan_term_months + \
                            (loan_amount - (monthly_interest_rate * (loan_term_months - month + 1))) * monthly_interest_rate
    return differentiated_payment





# Расчет дифференцированного платежа для первых 12 месяцев

#print(f"Месяц 1: {payment:.2f} ₽")