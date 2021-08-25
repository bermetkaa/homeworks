



names=[]
numbers=[]


lst=[20,50,100,'Тоголок Молдо','Курманжан Датка','Токтогул Сатылганов']
lst.append('Алыкул Осмонов')
lst.append(200)
print(lst)

for i in lst:
    if type(i)==str:
        names.append(i)
    elif type(i)==int:
        numbers.append(i)
print('Программа завершена')

print(names)
print(numbers)
lst=tuple(lst)

print(lst)

my_dict=dict(zip(names,numbers))
print(my_dict)

