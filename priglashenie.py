test = []

class Bron:
    def __init__(self):
        print(" введи имя того кого хочешь пригласить.\n")
        red = input()
        test.append(red)

        print('итак приглашены ' + str (test))
        red = input ("добавить кого-то ? да/нет' \n")
        print('вы выбрали ', red)
        print('итак приглашены ' + str(test))
        print('всего ' + str(len(test)) + ' человек') #функция len суммирует количество в массиве

        if red == 'да':
            while red == 'да':
                red = Bron()
        else:
            print ('конец программы \n')

bro = Bron()