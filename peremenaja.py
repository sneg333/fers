#демонстрация переменных и метод format
age = 18
age_str = 'привет мне {0} лет \n'.format(age)
print (age_str)


age = 20
ferst_name = 'Никита'
age_str = 'меня зовут {name} мне {age} лет \n' .format(age=age, name=ferst_name)
print (age_str)

# переменные и списки
pers = [10, 20, 30]

print ('лет {p[0]}'.format(p=pers))
print ('лет {p[1]}'.format(p=pers))
print ('лет {p[2]}'.format(p=pers))
print ('------------------------')
# переменные и словари

pers = {'иванов': 20, 'сидоров': 30, 3: '25'}

print ('лет {p[иванов]}'.format(p=pers))
print ('лет {p[сидоров]}'.format(p=pers))
print ('лет {p[3]}'.format(p=pers))
print ('------------------------')