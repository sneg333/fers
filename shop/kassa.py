# внесение данных в файл, метод первый а+, что бы можно было добавлять данные нужно добавить символ а
# режим одновременного чтения и дозаписи а+
# метод seek(0) сдвигает курсор в начало файла, и отображается все данные

f = open('kassa.txt', 'a+')
f.seek(0)
s = f.read()
print (s)
# добавляем в наш список новый продукт
f.write('\nmoloko')
print ('--------------------------------------')


# второй метод w+ стерает все данные которые были записаны в файле ранее,
# + в том что он создаёт файл если его не было

l = open('kassa2.txt', 'w+')
x = l.read()
l.write('moloko')
print (l)


