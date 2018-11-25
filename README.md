Описание
--------
Интерфейс блога содержится в пакете `blog/blogs.py`

Файл настроек `blog/settings.py`

Примеры использования/тесты `tests/test.py`

Создание и управление бд `blog/blog_manager.py` - запускается перед тестами

# Основное задание
8 баллов

Должны быть доступны следующие методы:

* добавить пользователя
* авторизоваться пользователем по логину + паролю
* получить полный список пользователей
* создать блог
* редактировать блог
* удалить блог (или отметить блог удаленным)
* получить список не удаленных блогов
* получить список не удаленных блогов созданный авторизованным пользователем
* создать пост связанный с одним или несколькими блогами
* отредактировать пост, должна быть возможность изменить заголовки/текст/блоги в которых опубликован
* удалить пост
* добавить комментарий если пользователь авторизован
* комментарии должны реализовывать поддержку веток комментариев ( комментарий можно оставить на пост или на другой комментарий )
* получить список всех комментариев пользователя к посту

хранение данных организовать в MySQL

# Доп задание №1

3 балла

наполнить базу данных данными:

* пользователи: 1000
* блоги: 100
* посты: 10000
* комментарии: 100000

# Доп задание №2
3 балла
* добавление необходимых индексов, обоснование добавленных индексов запросами
* оптимизация запросов, разбор нескольких запросов с помощью explain

дополнить класс методами: 

* получения ветки комментариев начиная с заданного
* получения всех комментариев для 1 или нескольких указанных пользователей из указанного блога

Результат
--------

для сдачи дз необходимо:
* прислать класс реализующий методы и sql запросы
* скрипт создающий базу данных
* Доп задание №1 скрипт наполняющий базу
* Доп задание №2 скрипт добавляющий индексы, разбор интересных запросов
