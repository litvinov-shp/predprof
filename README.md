# Job Analytics


## Описание

Этот проект анализирует файл `vacancy.csv`.

`vacancy.csv` выглядит следующим образом:  
Зарплата ; Тип контракта (трудоустройства) ; Размер компании ;
Название вакансии ; Название компании  
Разделитель - ";" (без кавычек)


## Установка

Для установки скачайте данный проект (`Code` -> `Download zip`)

Или склонируйте его с помощью `git clone`:  
`git clone https://github.com/litvinov-shp/predprof.git`


## Запуск

Зайдите в папку с этим проектом, откройте в ней терминал или
командную строку и введите:
`python <номер скрипта>.py`

Например:  
`python 1.py`  
Или  
`python 3.py`


## Использование

На данный момент в проекте есть 2 скрипта: `1.py` и `3.py`:

`1.py` - Записывает в файл vacancy_new.csv 3 самые оплачиваемые професии и выводит их на экран в формате <компания> - <вакансия> - <зарплата>  

`3.py` - Выводит информацию о сотрудниках компании, введённой пользователем, пока пользователь не введёт "None" (без кавычек)
