from fastapi import FastAPI
from routes import users, menu, addresses

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(menu.router, prefix="/menu", tags=["Menu"])
app.include_router(addresses.router, prefix="/addresses", tags=["Addresses"])

@app.get("/")
def root():
    return {"message": "Welcome to the Restaurant API"}