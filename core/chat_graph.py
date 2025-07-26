from langchain_groq.chat_models import ChatGroq
from langchain.schema import HumanMessage, AIMessage
from langgraph.graph import StateGraph, END
from typing import List, TypedDict
import os

class ChatState(TypedDict):
    messages: List

llm = ChatGroq(model="gemma2-9b-it", api_key="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")

def chatbot_node(state: ChatState) -> ChatState:
    response = llm(state["messages"])
    return {"messages": state["messages"] + [response]}

graph = StateGraph(ChatState)
graph.add_node("chatbot", chatbot_node)
graph.set_entry_point("chatbot")
graph.add_edge("chatbot", END)  # 1 reply per request (no infinite loop)

chat_graph = graph.compile()