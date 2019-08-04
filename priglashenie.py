test = []

class Bron:
    def __init__(self):
        print(" введи имя того кого хочешь пригласить.\n")
        red = input()
        test.append(red)

        print('итак приглашены ' + str (test))
        red = input ("добавить кого-то ? да, не добавлять - нет' \n")
        print('вы выбрали ', red)
        print('итак приглашены ' + str(test))
        print('всего ' + str(len(test)) + ' человек') #функция len суммирует количество в массиве

        if red == 'да':
            while red == 'да':
                red = Bron()
        else:
            print ('конец программы \n')

bro = Bron()

# второй вариант, более плный
test = []

class Bron:
    def __init__(self):
        red = input("добавить кого-то ? да, не добавлять ? - нет', удалить из списка? - уд \n")
        print('вы выбрали ', red)

        if red == 'да':
            ima = input("введите имя того кого хотите добавить \n")
            test.append(ima)
            print('итак приглашены ' + str(test))
            print('всего ' + str(len(test)) + ' человек')  # функция len суммирует количество в массиве
            while red == 'да':
                red = Bron()
        elif red == 'уд':
            ima = input("введите имя того кого хотите удалить \n")
            test.remove(ima)
            print('итак приглашены ' + str(test))
            print('всего ' + str(len(test)) + ' человек')  # функция len суммирует количество в массиве
            while red =='уд':
                red = Bron()
        else:
            print ('конец программы \n')

bro = Bron()