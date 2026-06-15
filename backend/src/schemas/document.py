from pydantic import BaseModel

class DocumentOut(BaseModel):
    id: int
    title: str
    file_type: str
    file_size: int
    status: str

