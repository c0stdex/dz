from datetime import datetime

def get_days_from_today():
    try:
    
        user_input = input("Введіть дату у форматі 'РРРР-ММ-ДД': ")
        
        
        target_date = datetime.strptime(user_input, '%Y-%m-%d')
        
        
        current_date = datetime.today()
        
        
        days_difference = (current_date - target_date).days
        
      
        return days_difference
    except ValueError:
      
        return "Використовуйте 'РРРР-ММ-ДД'."




result = get_days_from_today()

if isinstance(result, int):
    print(f"Різниця між заданою датою та сьогодні становить {result} днів.")
else:
    print(result)
