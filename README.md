A simple GUIless, REST API implemented in Python with FastAPI framework, for managing personal journal entries.

REST Endpoints:

| Metodă | URL             | Descriere                  | Status |
| ------ | --------------- | -------------------------- | ------ |
| POST   | `/entries/`     | Creează o intrare nouă     | Done   |
| GET    | `/entries/`     | Returnează toate intrările | Done   |
| GET    | `/entries/{id}` | Returnează o intrare       | Done   |
| PUT    | `/entries/{id}` | Actualizează o intrare     | Done   |
| DELETE | `/entries/{id}` | Șterge o intrare           | Done   |

Journal app main entity fields:
- id
- title
- content
- created_ad
- tags

Project tree:
jurnal_api/
├── main.py
├── models.py
├── database.py
└── requirements.txt

RUN THE APP: uvicorn main:app --host 127.0.0.1 --port 8000 --reload

DELETE req: http DELETE http://127.0.0.1:8000/entries/<id>

POST req (add): 
http POST http://127.0.0.1:8000/entries/ \
    title="New Entry" \
    content="Today I learned about HTTP methods in Linux!" \
    tags:='["linux", "httpie", "fastapi"]'

PUT req (update): 
http PUT http://127.0.0.1:8000/entries/f8dc     title="Updated Entry"     content="Updated content here"     tags:='["put", "update"]'
