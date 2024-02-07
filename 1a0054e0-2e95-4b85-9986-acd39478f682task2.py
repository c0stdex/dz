import random

def get_numbers_ticket(minimum, maximum, quantity):
 
    if not (1 <= minimum <= maximum <= 1000 and 1 <= quantity <= maximum - minimum + 1):
        print("Некоректні вхідні параметри.")
        return []

  
    random_numbers = random.sample(range(minimum, maximum + 1), quantity)

    
    return sorted(random_numbers)


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)


