import datetime
with open('text.txt', 'a') as a:
    start = 0
    end = 100
    count = 0
    time_s = datetime.datetime.now()
    while True:
        center = (start + end) // 2
        count += 1

        answer = input(f'Is your number: {center}? | greater/less/yes ')
        if answer == 'yes':
            print(f'Guessed in {count} attempts!')
            time_f = datetime.datetime.now() -  time_s
            a.write(f'{time_s} \n')
            a.write(f'{datetime.datetime.now()} \n')
            a.write(f'Guessed in {count} attempts! \n {time_f} \n')
            break
        elif answer == 'g':
            start = center + 1
        elif answer == 'l':
            end = center - 1

















