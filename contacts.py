contacts = {
    "Андрей Иванов" : "+798456545654",
    "Андрей Курочкин" : "+79874561232",
    "Анита Цой" : "+78712354565454"
    }

testing = input ('кого ищем ? ')

if testing in contacts:
    print ('контакт найден : ' + contacts[testing])
else:
    print ('контакт не найден')