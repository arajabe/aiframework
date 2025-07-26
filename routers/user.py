from fastapi import APIRouter
from pydantic import BaseModel
from langchain.schema import HumanMessage, AIMessage
from core.chat_graph import chat_graph
from core.db import save_message, load_history

user = "/user"

rotuer = APIRouter(prefix="/user", tags=["user"])

sessions = {}

