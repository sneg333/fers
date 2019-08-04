
class Bron:
    def __init__(self):
        print(" заказать платья.\n")
        fio = input("введи название ")
        vozrast = input("введи размер ")
        print('вы выбрали  ', fio, '\nваш размер - ', vozrast,)
        vibor = input ("хотите дозаказать платье? да или нет \n")
        print('вы выбрали ', vibor)

        if vibor == 'да':
            while vibor == 'да':
                vibor = Bron()
        else:
            print ('конец программы \n')


bro = Bron()