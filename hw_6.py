''' Пользователь загадывает число до 100, а программа должна угадать это число за
минимальное количество попыток. Программа дложна выдавать числа, а пользователь отвечать
больше, меньше или да
'''

min=0
max=100
sred=(min+max)//2
while True:
    print('ваше число меньше или больше',sred)
    x=input()
    if x=='big':
        min=sred
        sred=(min+max)//2
    elif x=='low':
        max=sred
        sred=(min+max)//2
    elif x=='Yes':
        print('я угадал число')
        break
