pogoda = 'дождь'
time = 'ночь'

if pogoda == 'дождь' and time == 'ночь':
    print ('верно')
    print ('программа заверщена')
    print ('----------------------------------------')



test = ['vasia', 'ola', 'peta']

print ('когда в списке по умолчанию что-то уже есть')
print ('введи имя тех кто был на вечеринке')
red = input()
if red in test:
    print (red + ', да верно')
    print ('----------------------------------------')
else:
    print ('Таких нет')
    print ('программа заверщена')
    print ('----------------------------------------')

test = []
print ('если список пустой изначально')

print ('введи имя того кого хочешь пригласить ')
red = input()
test.append(red)
print ('итак приглашены ' + str (test))

print ('введи имя тех кто был на вечеринке')
red = input()
if red in test:
    print (red + ', да верно')
    print ('----------------------------------------')
else:
    print ('Таких нет')
    print ('программа заверщена')
    print ('----------------------------------------')
