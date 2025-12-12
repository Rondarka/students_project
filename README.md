# students_project

Набор лабораторных работ по Python и Django.

## Состав репозитория

- `students_project/` — лабораторная работа №1 и №2 (первый Django‑проект, шаблоны и статика).
- `lab3/blog/` — лабораторная работа №3 (блог с моделью Article, админкой и архивом статей).
- `flatpages/` — приложение из лабораторной работы №2.
- `db.sqlite3`, `db_students.sqlite3` — базы данных для проектов.

## Используемый стек

- Python 3.10  
- Django 5.x  
- SQLite

## Как запустить проекты

Первая и вторая лабораторные:

cd students_project
py -3.10 manage.py runserver


Третья лабораторная:

cd lab3/blog
py -3.10 manage.py runserver

После запуска проекты доступны по адресу `http://127.0.0.1:8000/`.
