def calc():
    calcus = str(input('Введите выражение: '))
    if calcus == 'exit':
        exit
    else:
        x=calcus.split('+')
        print(int(x[0])+int(x[1]))

if __name__ == '__main__':
    calc()
