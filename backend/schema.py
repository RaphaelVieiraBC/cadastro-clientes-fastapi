from datetime import datetime

from pydantic import BaseModel, EmailStr


class ClienteBase(BaseModel):
    nome: str
    email: EmailStr
    telefone: str | None = None
    endereco: str | None = None


class ClienteCreate(ClienteBase):
    """Usado para criação de cliente (POST)."""
    pass


class ClienteUpdate(BaseModel):
    """Usado para atualização de cliente (PUT/PATCH)."""
    nome: str | None = None
    email: EmailStr | None = None
    telefone: str | None = None
    endereco: str | None = None


class ClienteOut(ClienteBase):
    id: int
    data_cadastro: datetime

    class Config:
        from_attributes = True  # permite criar a partir de modelos ORM (SQLAlchemy)