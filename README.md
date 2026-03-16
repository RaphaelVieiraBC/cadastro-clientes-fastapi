# Cadastro de Clientes – FastAPI + SQLAlchemy

API REST para cadastro e gerenciamento de clientes, construída com **FastAPI**, **SQLAlchemy** e **SQLite**.  
O projeto serve como base para estudos e para construção de aplicações reais de cadastro (CRM simples, sistemas internos, etc.).

---

## Tecnologias utilizadas

- **Python 3.11+** (ou versão que você estiver usando)
- **FastAPI** – framework web para construção da API
- **Uvicorn** – servidor ASGI
- **SQLAlchemy** – ORM para acesso ao banco de dados
- **SQLite** – banco de dados padrão (pode ser trocado por PostgreSQL)
- **Pydantic / Pydantic Settings** – validação de dados e configurações
- **email-validator** – validação de e-mail usada pelo `EmailStr`

---

## Estrutura do projeto

```text
.
├── backend/
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py        # Configurações (DATABASE_URL, etc.)
│   ├── routers/
│   │   ├── __init__.py
│   │   └── clientes.py        # Rotas de clientes (CRUD)
│   ├── tests/                 # (reservado para testes)
│   ├── __init__.py
│   ├── crud.py                # Funções de acesso a dados (CRUD)
│   ├── database.py            # Engine, SessionLocal, Base, get_db
│   ├── main.py                # Aplicação FastAPI
│   ├── models.py              # Modelos SQLAlchemy (Cliente)
│   └── schema.py              # Schemas Pydantic (ClienteCreate, ClienteOut, etc.)
├── frontend/                  # (reservado para futura interface)
├── requirements.txt
└── README.md
```

---

## Funcionalidades

- **Cadastro de clientes**
  - Nome, e-mail, telefone, endereço, data de cadastro.
  - Validação de e-mail com `EmailStr`.

- **CRUD completo**
  - `POST /clientes/` – criar cliente
  - `GET /clientes/` – listar clientes (com paginação básica `skip` e `limit`)
  - `GET /clientes/{id}` – obter cliente por ID
  - `PUT /clientes/{id}` – atualizar dados do cliente
  - `DELETE /clientes/{id}` – remover cliente

- **Documentação automática**
  - Swagger UI em: `http://127.0.0.1:8000/docs`
  - ReDoc em: `http://127.0.0.1:8000/redoc` (opcional, se habilitado)

---

## Como rodar o projeto localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/cadastro-clientes-fastapi.git
cd cadastro-clientes-fastapi
```

(Substitua pela URL do seu repositório.)

### 2. Criar e ativar um ambiente virtual

```bash
python -m venv venv
# Windows (PowerShell):
.\venv\Scripts\Activate.ps1
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente (opcional)

Por padrão, o projeto usa **SQLite** em um arquivo local.

Você pode criar um arquivo `.env` na raiz (baseado em `.env.example`):

```env
DATABASE_URL=sqlite:///./clientes.db
```

Para usar PostgreSQL (exemplo):

```env
DATABASE_URL=postgresql://usuario:senha@localhost:5432/nome_do_banco
```

### 5. Rodar a aplicação

```bash
uvicorn backend.main:app --reload
```

Acesse:

- `http://127.0.0.1:8000` – rota raiz
- `http://127.0.0.1:8000/docs` – documentação interativa (Swagger)

---

## Endpoints principais

- **Saúde / raiz**
  - `GET /` → mensagem simples confirmando que a API está rodando.

- **Clientes**
  - `POST /clientes/` → cria um novo cliente.
  - `GET /clientes/` → retorna lista de clientes.
  - `GET /clientes/{cliente_id}` → retorna um cliente específico.
  - `PUT /clientes/{cliente_id}` → atualiza um cliente.
  - `DELETE /clientes/{cliente_id}` → exclui um cliente.

---

## Próximos passos / ideias de evolução

- Autenticação e autorização (JWT, OAuth2).
- Paginação mais robusta e filtros por nome/e-mail.
- Integração com um banco relacional em produção (PostgreSQL, MySQL).
- Criação de um **frontend** (React, Vue, etc.) consumindo essa API.
- Adicionar testes automatizados (pytest) para os endpoints.
