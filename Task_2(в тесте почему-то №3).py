import random
from typing import List
def get_unique_list_numbers() -> List[int]:
    random_int = random.sample(range(-10, 10), 15)  # TODO написать функцию для получения списка уникальных целых чисел
    return random_int


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))