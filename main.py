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
    return "Hello, and welcome to this RESTful API app"

#create a new entry with POST
@app.post("/entries/")
def create_entry(entry: JournalEntry):
    entry_id = str(uuid4())
    add_entry(entry_id, entry)
    return {"id": entry_id, "entry": entry}

#list all entried with get
@app.get("/entries/")
def read_entries():
    return load_db()
