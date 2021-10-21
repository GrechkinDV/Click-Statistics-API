# To start project:

- pip install -r requirements.txt
- python manage.py runserver

В качестве базы данных оставлен дефолтный SQLite3
API имеет несколько endpoint'ов:

1. Сохранение статистики
   URL: http://localhost:8000/api/click-statistic/
   Method: POST
   Данные: {
   "views": {VIEWS},
   "clicks": {CLICKS},
   "cost": {COST},
   }
2. Метод показа статистики
   URL: http://localhost:8000/api/click-statistic/?from={from_date}&to={to_date}
   Method: GET
3. Метод удаления всеё статистики
   URL: http://localhost:8000/api/click-statistic/delete_all/
   METHOD: DELETE
4. Метод удаления определённого объекта статистики
   URL: http://localhost:8000/api/click-statistic/{ID}/
   METHOD: DELETE

Чтобы запустить тесты:
pytest stats/tests
