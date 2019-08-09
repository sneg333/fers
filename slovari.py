# словарь
d = {'name': 'Иванов', 'marshrut': '93', 'avtobus': [13,45,78], 'ben': True, 0:[]}

#вызываем данное по ключу
print (d['name'])
#
vvedikl = input('введи ключ ')
vvedizn = input('введи значение ')
d[vvedikl] = vvedizn
print (d)

# добавить значение в словарь
new_kl = input('введи новый ключ ')
d[new_kl] = 55
print (d)

#провериить есть ли пара ключ значение в списке метод get
prover_kl = input('введи ключ и мы узнаем есть ли такая пара ключ - элемент ')
print (d.get(prover_kl, 'такого нет'))
