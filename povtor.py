# повтор функции
def print_spam():
    print('spam')
    print('spam')
    print('spam')

print_spam()


def max(x, y):
    if x > y:
        return x
    else:
        return y

print (max( 5, 6 ))


def port():
    asd = 'assa'
    print (asd)

port()

haydi = 'риивет хауди'

print (haydi)

def houdiho(nominto):
    '''функция'''
    print ('ho ho ' + nominto())

def dva():
    '''вложенная функция'''
    return 'вложение ' + input("введи имя \n")

houdiho(dva)

def trava (ima):
    print ('veru ' + ima)

vibor = input ("введи имя \n")
trava(vibor)