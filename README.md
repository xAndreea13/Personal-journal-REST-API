A simple GUIless, REST API implemented in Python with FastAPI framework, for managing personal journal entries.

REST Endpoints:

| Metodă | URL             | Descriere                  |
| ------ | --------------- | -------------------------- |
| POST   | `/entries/`     | Creează o intrare nouă     |
| GET    | `/entries/`     | Returnează toate intrările |
| GET    | `/entries/{id}` | Returnează o intrare       |
| PUT    | `/entries/{id}` | Actualizează o intrare     |
| DELETE | `/entries/{id}` | Șterge o intrare           |

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