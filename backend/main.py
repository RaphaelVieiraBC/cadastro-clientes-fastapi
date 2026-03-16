from fastapi import FastAPI
from backend.database import Base, engine
from backend.routers import clientes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cadastro de Clientes", version="1.0.0")

app.include_router(
    clientes.router,
    prefix="/clientes",
    tags=["clientes"],
)



@app.get("/")
def root():
    return {"message": "API de Cadastro de Clientes"}