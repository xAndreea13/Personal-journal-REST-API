from fastapi import FastAPI, HTTPException
from models import JournalEntry, JournalEntryUpdate
from typing import Dict
from uuid import uuid4
from database import *
from fastapi.responses import PlainTextResponse

# the entry points are defined here

# we create a new FastAPI instance
app = FastAPI()
#initiate the json database
init_db()

#for the root of project
@app.get("/", response_class=PlainTextResponse)
def print_message():
    return "Hello, and welcome to this RESTful API"

#create a new entry with POST
@app.post("/entries/")
def create_entry(entry: JournalEntry):
    entry_id = str(uuid4())[:4]
    add_entry(entry_id, entry)
    return {"id": entry_id, "entry": entry}

#list all entried with get
@app.get("/entries/")
def read_entries():
    return load_db()

#get a certain entry
@app.get("/entries/{entry_id}")
def read_entry(entry_id: str):
    if check_id(entry_id) == False:
        raise HTTPException(status_code=404, detail="Entry not found")
    return return_entry(entry_id)

@app.put("/entries/{entry_id}")
def update_entry(entry_id: str, update: JournalEntryUpdate):
    if not check_id(entry_id):
        raise HTTPException(status_code=404, detail="Entry not found")

    existing = return_entry(entry_id)  # This returns a dict
    existing_model = JournalEntry(**existing)  # Convert to Pydantic model

    updated_model = existing_model.copy(update=update.dict(exclude_unset=True))

    update_db_entry(entry_id, updated_model)

    return updated_model

@app.delete("/entries/{entry_id}")
def delete_entry(entry_id: str):
    if check_id(entry_id) == False:
        raise HTTPException(status_code=404, detail="Entry not found")
    delete_db_entry(entry_id)
    return {"detail": "Entry deleted"}