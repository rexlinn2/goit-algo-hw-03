import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000:
        return []
    if min > max:
        return []
    if quantity < 0 or quantity > (max - min + 1):
        return []
    
    numbers = random.sample(range(min, max + 1), quantity)
    
    numbers.sort()
    
    return numbers


lottery_numbers = get_numbers_ticket(1, 99, 5)
print("Ваші лотерейні числа:", lottery_numbers)