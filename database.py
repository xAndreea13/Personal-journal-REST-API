import json
from typing import Dict
from models import JournalEntry
from pathlib import Path

# we check if json file exist
DB_FILE = Path("journal.json")

#init the database
def init_db():
    if not DB_FILE.exists():
        DB_FILE.touch()
        with open("journal.json", "w") as f:
            json.dump({}, f, indent=3)
    else:
        print("Database found!\n")

#load database
def load_db():
    if DB_FILE.exists():
        with open(DB_FILE, "r") as f:
            data = json.load(f)
            return data

#add an entry to the database
def add_entry(entry_id: str, entry: JournalEntry):
    data = {}

    # Load existing data if the file exists and is not empty
    if DB_FILE.exists():
        with open(DB_FILE, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}

    # Add the new entry
    data[entry_id] = entry.dict()

    # Overwrite the file with the updated data
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=3)
        f.truncate()

#delete an entry from the database
def delete_db_entry(entry_id):
    if DB_FILE.exists():
        with open(DB_FILE, "r+") as f:
            data = json.load(f)

            if entry_id in data:
                del data[entry_id]
                f.seek(0)
                json.dump(data, f, indent=3)
                f.truncate()
                return True
            else:
                return False
    return False


#update an entry from database
def update_db_entry(entry_id, entry):
    if DB_FILE.exists():
        with open(DB_FILE, "r+") as f:
            data = json.load(f)
            if entry_id in data:
                data[entry_id]["title"] = entry.title
                data[entry_id]["content"] = entry.content
                data[entry_id]["tags"] = entry.tags or []  # Replace entirely
            f.seek(0)
            json.dump(data, f, indent=3)
            f.truncate()

def check_id(entry_id):
    if DB_FILE.exists():
        with open(DB_FILE, "r") as f:
            data = json.load(f)
            if entry_id not in data:
                return False
            else:
                return True

def return_entry(entry_id):
    if DB_FILE.exists():
        with open(DB_FILE, "r") as f:
            data = json.load(f)
            if entry_id in data:
                return data[entry_id]