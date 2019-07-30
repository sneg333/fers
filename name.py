# -*- coding: utf-8 -*-
# klik = 'y'
# while klik == 'y':
#     vibor = input("хотите посмотреть все гостиници? y или n \n")
#     print(vibor)

print(" выбор места жилья.\n")


class Bron:
    def kino(self):
        fio = input("введи ваше имя \n")
        vozrast = input("введи ваш возраст \n")
        print(fio, vozrast,)

vibor = input( "забронировать место? если да то введите y, если нет, введите n \n")

if vibor == 'y':
    fio = input("введи ваше имя \n")
    vozrast = input("введи ваш возраст \n")
    print(fio, vozrast, )
    print('место забронированно')

    eche =  input("хотите дозаказать бронь? y или n \n")
    if eche == 'y':
        while vibor == 'y':
            vibor = input("хотите дозаказать бронь-2? y или n \n")

        else:
            print('нет')

    else:
        print('конец программы, вы не захотели смотреть платья и нажали n')

print('конец после первой n')



#
# if vibor == 'y':
#     while vibor== 'y':
#         vibor = input("хотите дозаказать бронь-2? y или n \n")
#
#     else:
#         print('нет')
#
# else:
#     print('конец программы, вы не захотели смотреть платья и нажали n')





