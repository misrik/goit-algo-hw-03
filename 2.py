import random

def get_numbers_ticket(minimum, maximum, quantity):
    # Перевірка валідності вхідних параметрів
    if not (1 <= minimum < maximum <= 1000 and 1 <= quantity <= maximum - minimum + 1):
        return []

    # Унікальний набір чисел у заданому діапазоні
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(minimum, maximum))

    # Множина у відсортований список
    sorted_numbers = sorted(list(numbers))
    
    return sorted_numbers

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

