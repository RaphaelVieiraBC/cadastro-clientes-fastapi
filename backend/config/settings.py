"""
Configurações da aplicação (variáveis de ambiente, URL do banco, etc.).
Preencha conforme seu ambiente; use .env na raiz do projeto.
"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Configurações carregadas de variáveis de ambiente."""

    # API
    API_V1_PREFIX: str = "/api/v1"
    PROJECT_NAME: str = "Cadastro de Clientes"

    # Banco de dados
    DATABASE_URL: str = "sqlite:///./clientes.db"

    class Config:
        env_file = ".env"
        case_sensitive = True
