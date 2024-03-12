from datetime import datetime, timedelta

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d')
        today = datetime.today()
        delta = today - input_date
        # Перевірка, чи введена дата пізніша за поточну
        if input_date > today:
            delta = input_date - today
            return -delta.days
        else:
            return delta.days
    except ValueError:
        return "Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'."

print(get_days_from_today("2025-03-11"))  

