# test_up
UpTrader test task

# 

Древовидного меню на Django
# **test_up**

ТЗ 
```
Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:
1) Меню реализовано через template tag
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django
5) Активный пункт меню определяется исходя из URL текущей страницы
6) Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8) На отрисовку каждого меню требуется ровно 1 запрос к БД
Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.
 {% draw_menu 'main_menu' %}
При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.
При решении тестового задания у вас не должно возникнуть вопросов. Если появляются вопросы, вероятнее всего, у вас недостаточно знаний.
Задание выложить на гитхаб.
```

### **Стек**
![python version](https://img.shields.io/badge/Python-3.10-green)
![django version](https://img.shields.io/badge/Django-4.17-blue)


### **Запуск проекта в dev-режиме**

1. Клонируйте репозиторий и перейдите в него в командной строке:

```
git clone git@github.com:VugarIbragimov/test_up.git
```

2. Установите и активируйте виртуальное окружение
```
python -m venv .venv
``` 

```
для windows:
source .venv/Scripts/activate

для Mac:
source .venv/bin/activate
```

3. Установите зависимости из файла requirements.txt в каталоге menu
```
pip install -r requirements.txt
```

4. В папке с файлом manage.py выполните миграции:
```
python manage.py makemigrations
python manage.py migrate
```

5. Создайте суперюзера, зайдите в админку
```
python manage.py createsuperuser
```
6. Создайте тестовые данные для отрисовки меню
```
С названием(title) main_menu и main_menu_2
```

7. В папке с файлом manage.py запустите сервер, выполнив команду:
```
python manage.py runserver
```

8. Откройте страницу по адресу http://127.0.0.1:8000/main_menu/


### **Запуск проекта с помощью Docker**

1. Перейдите в директорию с Dcokerfile и соберите образ:

```
docker build -t tree .
```

2. Запустите контейнер:
```
docker run --name tree --rm -p 8000:8000 tree
``` 

3. В папке с файлом manage.py выполните миграции:
```
docker exec tree python manage.py makemigrations
docker exec tree python manage.py migrate  
```

4. Создайте суперюзера, зайдите в админку
```
docker exec tree python manage.py createsuperuser
```
5. Создайте тестовые данные для отрисовки меню
```
С названием(title) main_menu и main_menu_2
http://localhost:8000/admin/login/?next=/admin/
```
6. Откройте страницу по адресу http://localhost:8000/main_menu/