from fastapi import APIRouter
from pydantic import BaseModel
from core.db import get_db_connection

router = APIRouter(prefix="/contact", tags=["contact"])

class ContactForm(BaseModel):
    name: str
    email: str
    message: str

@router.post("/")
def save_contact(form: ContactForm):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)",
        (form.name, form.email, form.message)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return {"status": "saved"}