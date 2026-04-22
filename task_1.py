from datetime import datetime

def get_days_from_today(date):
    given_date = datetime.strptime(date, "%Y-%m-%d").date()
    today = datetime.today().date()
    return (today - given_date).days

print(get_days_from_today("2026-04-21"))