from fastapi import APIRouter
from core.db import get_db_connection

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get("/conversations")
def list_conversations():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, session_id, sender, message, timestamp FROM conversations ORDER BY id ASC")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return {"conversations": rows}