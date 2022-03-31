
def shout_on_me():
    shout = str(input('Что ты сказал? '))
    if shout == 'exit':
        exit
    else:
        print('От',shout.upper(),'слышу')

if __name__=='__main__':
    shout_on_me()