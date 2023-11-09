Задание №1
-Реализована логика из требований ТЗ;
-Запуск проекта: docker-compose up --b
'''http://localhost:8000/'''
GET запрос 'check_data/?phone=' - полученние данныз по номеру телефона
POST запрос '/write_data' с телом
(phone:’89090000000’
address:’текстовый адрес’) - запись в бд
PUT запрос '/write_data' с телом
(phone:’89090000000’
address:’текстовый адрес’) - обновление данных



Задание №2
'''UPDATE full_names AS fn
SET status = sn.status
FROM short_names AS sn
WHERE SUBSTRING(fn.name, 1, charindex('.',fn.name)-1) = sn.name;'''

В этом скрипте мы обновляем поле status в таблице full_name используя SUBSRTING.
Получаем поле name в таблице full_name без расширения, то есть получаем имя до точки,
сравниваем имя без расширения с именем из таблицы short_name и обновляем данные в поле status 
таблице full_name.