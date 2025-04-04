from users import router as users_router
from menu import router as menu_router
from addresses import router as addresses_router

app = FastAPI()

app.include_router(users_router, prefix="/users")
app.include_router(menu_router, prefix="/menu")
app.include_router(addresses_router, prefix="/addresses")


@app.get("/")
def root():
    return {"message": "Welcome to the Restaurant API"}
