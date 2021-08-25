import datetime
import random

number = random.randint(1, 100)
count = 0
time_s = datetime.datetime.now()
a = open('text.txt', 'a', encoding='UTF-8')

while True:
    count += 1
    try:
        guess = int(input('Guess the number '))
    except ValueError:
        print('Вводите целые числа!')
        continue
    if guess == number:
        print(' Yes! You guessed the number in {} attempts'.format(count))
        time_f = datetime.datetime.now() - time_s
        a.write(f'{time_s} \n')
        a.write(f'{datetime.datetime.now()} \n')
        a.write(f'Guessed in {count} attempts! \n {time_f} \n')
        a.close()
        break

    elif guess <= number - 3 and guess >= number + 3:
        if guess < number:
            print("it's very cold, bigger")
        elif guess > number:
            print("it's very cold, lower")

    elif guess <= number - 7 and guess >= number + 7:
        if guess < number:
            print("it's very cold, bigger")
        if guess > number:
            print("it's very cold, lower")

    elif guess < number + 30 and guess > 0 or guess > number + 30 and guess <= 100:
        if guess < number:
            print("it's very cold, bigger")
        elif guess > number:
            print("it's very cold, lower")
