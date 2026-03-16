from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from backend.database import Base


class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    telefone = Column(String, index=True)
    endereco = Column(String, index=True)
    data_cadastro = Column(DateTime, default=datetime.now)