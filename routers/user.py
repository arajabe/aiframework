from fastapi import APIRouter
from pydantic import BaseModel
from langchain.schema import HumanMessage, AIMessage
from core.chat_graph import chat_graph
from core.db import save_message, load_history

user = "/user"

router = APIRouter(prefix="/user", tags=["user"])

sessions = {}

class ChatRequest(BaseModel):
    session_id: str
    message: str

@router.post("/chat")
def chat(req: ChatRequest):

    ## Load the conversation history
    try:
        history = load_history(req.session_id)
        messages = [HumanMessage(content=msg) if sender == "User" else AIMessage(content=msg) for sender, msg in history]
        if req.session_id not in sessions:
            sessions[req.session_id] = {"messages": messages}

        # Add new message
        sessions[req.session_id]["messages"].append(HumanMessage(content=req.message))
        save_message(req.session_id, "User", req.message)

        # Get AI reply
        result = chat_graph.invoke(sessions[req.session_id])
        sessions[req.session_id] = result

        ai_reply = [m for m in result["messages"] if isinstance(m, AIMessage)][-1].content
        save_message(req.session_id, "Bot", ai_reply)

        return {"session_id": req.session_id, "reply": ai_reply}

    
    except Exception as e:
        return {"error": str(e)}

