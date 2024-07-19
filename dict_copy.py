'''
Метод copy() створює поверхневу копію словника. Якщо використати new_dict = my_dict.copy(), то new_dict буде новим словником з тими самими парами ключ-значення, що і my_dict, але як окремий об'єкт.


'''
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
new_dict = my_dict.copy()
print(new_dict) # {'name': 'Alice', 'age': 25, 'city': 'New York'}
