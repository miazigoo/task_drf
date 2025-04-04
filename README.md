# ТЗ минимальное API на Django REST Framework для работы с задачами

### Требования:
1. Создайте модель **Task** с полями:
    - `title` (строка, максимум 100 символов) – название задачи.
    - `is_completed` (логическое) – статус выполнения задачи (по умолчанию: `False`).
2. Реализуйте только два API-метода:
    - **_Получение списка задач_** (GET `/tasks/`).
    - **_Создание новой задачи_** (POST `/tasks/`).
3. Для валидации:
    - Поле `title` не может быть пустым.
4. Тестировать приложение не нужно.
### Результат выполнения:
1. Файлы `models.py`, `serializers.py`, `views.py`, `urls.py`.
2. Пример одного запроса на создание задачи и ответа на него в виде JSON.


## Как запустить:
[Установите Python](https://www.python.org/), если этого ещё не сделали.

Проверьте, что `python` установлен и корректно настроен. Запустите его в командной строке:
```shell
  python --version
```
**Важно!** Версия Python должна быть не ниже 3.9

Возможно, вместо команды `python` здесь и в остальных инструкциях этого README придётся использовать `python3`. Зависит это от операционной системы и от того, установлен ли у вас Python старой второй версии.

В каталоге проекта создайте виртуальное окружение:
```shell
  python -m venv venv
```
Активируйте его. На разных операционных системах это делается разными командами:

- Windows: `.\venv\Scripts\activate`
- MacOS/Linux: `source venv/bin/activate`


Установите зависимости в виртуальное окружение:
```shell
  pip install -r requirements.txt
```

Сделайте миграцию:
```shell
  python manage.py migrate
```

Запустите локальный сервер:
```shell
  python manage.py runserver
```

**Откройте вкладку** [http://127.0.0.1:8000/api/v1/tasks/](http://127.0.0.1:8000/api/v1/tasks/):
 - для post-запроса используйте следующий пример:
`{
"title": "Купить хлеб"
}`
 - При успешном добавлении вернет `{
    "status": "success"
}` и статус-кодом `201`
 - get-запрос вернет все таски со значением `is_completed=False` 

