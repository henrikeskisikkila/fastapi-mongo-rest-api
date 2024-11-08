import uuid
from pydantic import BaseModel, Field
from typing import Optional

class TodoItem(BaseModel):
  id: str = Field(default_factory=uuid.uuid4, alias='_id')
  title: str
  description: Optional[str] = None
  completed: bool = False