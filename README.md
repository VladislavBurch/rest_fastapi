# REST-ctрвис на FastAPI

To start server run `uvicorn my_project.main:app --reload`

Requirements:
1. __fastapi__
 > `pip install fastapi`
2. __uvicorn__
 > `pip install uvicorn`

__Address__: localhost:8000

__Example__: localhost:8000/products

---
## DataBase description (short):

Table: products

| id (primary key): int   |      Name: string      |  description: string |  is_available: bool |
|----------|:-------------:|:-------------:|------:|
| 1 |  name 1 | description 1 | true |
| 2 |  name 2 | description 2 |  true |
| 3 |  name 3 | description 3 | true |

## Ремарки

Файл `__init__.py` не явяется обязательным. Его рекомендует создавать документация FastAPI.
