from fastapi import FastAPI
from routers import user, admin, contact

app = FastAPI(title="Chatbot Framework")

# Register feature routes
app.include_router(user.router)
app.include_router(admin.router)
app.include_router(contact.router)

@app.get("/")
def root():
    return {"message": "Main API is running"}