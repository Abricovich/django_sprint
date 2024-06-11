# [Проект Blogicum"](https://github.com/Abricovich/the_snake/blob/main/the_snake.py)


## **Оглавление**

1. [Описание проекта](https://github.com/Abricovich/the_snake/blob/main/README.md#1-%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)
2. [Правила игры](https://github.com/Abricovich/the_snake/blob/main/README.md#2-%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D0%B0-%D0%B8%D0%B3%D1%80%D1%8B)
3. [Общая логика и компоненты](https://github.com/Abricovich/the_snake/blob/main/README.md#3-%D0%BE%D0%B1%D1%89%D0%B0%D1%8F-%D0%BB%D0%BE%D0%B3%D0%B8%D0%BA%D0%B0-%D0%B8-%D0%BA%D0%BE%D0%BC%D0%BF%D0%BE%D0%BD%D0%B5%D0%BD%D1%82%D1%8B-%D0%B8%D0%B3%D1%80%D1%8B)
4. [Установка и запуск](https://github.com/Abricovich/the_snake/blob/main/README.md#4-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0-%D0%B8%D0%B3%D1%80%D1%8B)

### 1. Описание проекта

**Blogicum** - социальная сеть для публикации личных дневников. Сайт, на котором пользователь может создать свою страницу и публиковать на ней сообщения («посты»). 

Для каждого поста нужно указать *категорию* — например «путешествия», «кулинария» или «python-разработка», а также опционально *локацию*, с которой связан пост, например «Остров отчаянья» или «Караганда».

Пользователь может перейти на страницу любой категории и увидеть все посты, которые к ней относятся.
Пользователи смогут заходить на чужие страницы, читать и комментировать чужие посты.

Для своей страницы автор может задать имя и уникальный адрес. Дизайн можно взять самый обычный, но красивый. Тексты без особой разметки.
Ещё надо иметь возможность модерировать записи и блокировать пользователей, если начнут присылать спам.

[⬆️к оглавлению](https://github.com/Abricovich/the_snake/blob/main/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 2. Общая логика и компоненты

За основу был взять фраймворк Django/

**blogicum** — непосредственно сам проект с приложениями:

- **pages** — это приложение понадобится для работы со статическими страницами проекта;
- **blog** — тут будет происходить вся работа с публикациями пользователей.

[⬆️к оглавлению](https://github.com/Abricovich/the_snake/blob/main/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 3. Установка и запуск

```bash
pip install -r requirements.txt
```

```python
python manage.py runserver
```

[⬆️к оглавлению](https://github.com/Abricovich/the_snake/blob/main/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)
