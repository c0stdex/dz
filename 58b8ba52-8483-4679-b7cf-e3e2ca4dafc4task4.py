from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
         
            birthday_this_year = birthday.replace(year=today.year + 1)

       
        days_until_birthday = (birthday_this_year - today).days

       
        if 0 <= days_until_birthday <= 7:
           
            if birthday_this_year.weekday() >= 5:
                
                next_monday = birthday_this_year + timedelta(days=(7 - birthday_this_year.weekday()))
                congratulation_date = next_monday.strftime("%Y.%m.%d")
            else:
                congratulation_date = birthday_this_year.strftime("%Y.%m.%d")

            
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date})

    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
