my_dict = {'Екатерина': 10, 'Анна': 8, 'Елена': 9, 'Анастасия': 7}
print(my_dict)
print(my_dict['Екатерина'])
print(my_dict.get('Наталья', '"Без ошибки"'))
my_dict.update({'Наталья': 11,
                'Нина': 9})
a = my_dict.pop('Нина')
print(a)
print(my_dict)

my_set = {1, 2, 2, 3, 3, 4, 5, 5, (1, 2, 3), (1, 2, 3), (2, 1, 3), True}
print(my_set)
my_set.add('Хомяк')
my_set.add(4.44)
my_set.remove((1, 2, 3))
print(my_set)
