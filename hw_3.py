""" Для выполнения этого задания вам помогут методы списков"""

# Покупки на сегодня
today = ["лемон", "блокнот", "кола", "ручка", "сигареты", "молоко", "лампочка"]

# Покупки на завтра
tomorrow = []

# Удалить сигареты из списка today
today.remove(today[4])
# Добавить все орехи из списка nuts в список today
nuts = ["фисташки", "грецкие орехи"]
today.extend(nuts)
# Заменить колу на максым
today[2]="максым"
# Вставить миндаль между фисташками и грецкими орехами
today.insert(7,'миндаль')
# Добавить курут в конец списка today
today.append('курут')
# Всё не съедобное переместить в покупки на завтра
tomorrow.extend(today)
tomorrow.pop(1)
tomorrow.pop(2)
tomorrow.pop(3)
today.pop(0)
today.pop(1)
today.pop(2)
today.pop(3)
today.pop(3)
today.pop(3)
today.pop()

print(today) # ['блокнот', 'ручка', 'лампочка']
print(tomorrow) # ['лемон', 'максым', 'молоко', 'фисташки', 'миндаль', 'грецкие орехи', 'курут']