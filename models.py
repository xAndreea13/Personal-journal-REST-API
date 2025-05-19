from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# defines data models using Pydantic, 
# which is a library used with FastAPI 
# to validate and serialize data automatically

# used for CREATING and RETURNING entries
class JournalEntry(BaseModel):
    title: str
    content: str
    tags: Optional[List[str]] = []
    create_at: str = datetime.now().isoformat()

# used specifically for UPDATING a journal entry
class JournalEntryUpdate(BaseModel):
    title: Optional[List[str]]
    content: Optional[List[str]]
    tags: Optional[List[str]]
