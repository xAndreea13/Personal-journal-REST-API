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

PUT req (add): http POST http://127.0.0.1:8000/entries/ Content-Type:application/json --raw '{\"title\": \"Test2\", \"content\": \"Hello there world! it is a very beautiful day today!\", \"tags\": [\"fastapi\", \"python\"]}'

PUT req (update): 
