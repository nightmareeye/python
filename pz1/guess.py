import random

def guess():
    """Угадайка"""
    number = random.randint(0, 100)
    #print(number)
    while True:
        
        answer = str(input('Угадайте число: '))
        # если ввести не число, то всё поломается. Обработку ошибок рассмотрим позже
        
        if answer == 'exit':
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

if __name__ == '__main__':
    guess()