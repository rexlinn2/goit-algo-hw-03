from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta = today - given_date
        return delta.days
    except ValueError:
        return "Невірний формат дати. Використовуйте 'YYYY-MM-DD'"
    
print(get_days_from_today("2026-04-21"))