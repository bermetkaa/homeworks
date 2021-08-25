import random
from lesson_6 import plus
# print(plus(1, 2))

# while True:
#     request = input(''' Let's' Play? y/n' ''')
#     if request == 'y':
#         persons = int(input('How many people? '))
#         for player in range(persons):
#             first = random.randint(1, 6)
#             second = random.randint(1, 4)
#             res = first + second
#             print('{} + {}'.format(first, second))
#     elif request == 'n':
#         break




import random
number = random.randint(1, 100)
count = 0
while True:
    count += 1
    try:
        guess = int(input('Guess the number '))
    except ValueError:
        print('Вводите целые числа!')
        continue
    if guess == number:
        print(' Yes! You guessed the number in {} attempts'.format(count))
        break

    elif guess <= number-3 and guess>=number+3:
        print(' greater ')
        if guess<number:
            print('очень близко!больше')
        if guess>number:
            print('Очень близко!меньшe' )
    elif guess <=number-7 and guess>=number+7:
        if guess < number:
            print('очень близко!больше')
        if guess > number:
            print('Очень близко!меньше' )
    elif guess <= number- 15 and guess >=number + 15:
        print(' less ')


# islam=1
# bekbolsun=2
# esenbek=3
# a=(random.randint(1,3))
# if a==islam:
#     print('islam')
# elif a==bekbolsun:
#     print('beka')
# else:
#     print('esenbek')

