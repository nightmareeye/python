import random


def guess():
    """Угадайка"""
    number = random.randint(0, 100)
    print(number)
    while True:
        
        answer = str(input('Угадайте число: '))
        # если ввести не число, то всё поломается. Обработку ошибок рассмотрим позже
        
        if answer == 'exit':
            print('Завершаю, загаданное число:', number)
            return 1
        elif answer == 'q':
            print('Завершаю, загаданное число:', number)
            break
        elif answer.isdigit()==1:
            answer = int(answer)
            if answer == number:
                print('Успех')
                break
        
            elif answer < number:
                print('Бери выше')
            else:
                print('Бери ниже')
        else:
            print('Введено нечисловое значение, попробуйте снова')


def calc():
    """Калькулятор"""
    calcus = str(input('Введите выражение: '))
    if calcus == 'exit':
        return 1
    elif calcus == 'q':
        exit
    else:
        x=calcus.split('+')
        print(int(x[0])+int(x[1]))


def shout_on_me():
    """Крикни"""
    shout = str(input('Что ты сказал? '))
    if shout == 'exit':
        return 1
    elif shout == 'q':
        exit
    else:
        print('От',shout.upper(),'слышу')


def group_parser():
    """Определятор"""
    group = str(input('Введите номер группы:'))
    if not group.startswith('733'):
        print('Это не группа 3 курса')
        return 1
        
    if group.endswith('3'):
        print('%s - Третья группа' % group)
    elif group.endswith('4'):
        print('%s - Четверная группа' % group)
    elif group.endswith('5'):
        print('%s - Пятая группа' % group)
    else:
        print('%s - Непонятная группа' % group)
    answer = input('Попробуйте выйти: ')
    while True:
        answer = input('Неправильно! Попробуйте ещё раз: ')
        if answer == 'exit':
            print('Успех!')
            return 1
        elif answer == 'q':
            exit
            print('Успех!')


def main():
    dict = {'1. угадайка': guess, '2. калькулятор': calc, '3. определятор': group_parser, '4. крикни': shout_on_me}
    while True:
        print('Выберите Подпрограмму')
        for i in dict.keys():
            print(i)
        x=str(input())
        for key, vals in dict.items():
            if x.lower() in key:
                k=vals()
                if k==1:
                   return False


if __name__ == '__main__':
    main()