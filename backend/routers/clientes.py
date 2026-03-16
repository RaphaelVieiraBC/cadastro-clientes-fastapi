from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.database import get_db
from backend import crud, schema

router = APIRouter()


@router.post(
    "/",
    response_model=schema.ClienteOut,
    status_code=status.HTTP_201_CREATED,
)
def criar_cliente(
    cliente_in: schema.ClienteCreate,
    db: Session = Depends(get_db),
):
    existente = crud.get_cliente_by_email(db, cliente_in.email)
    if existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Já existe um cliente com este e-mail.",
        )

    cliente = crud.create_cliente(db, cliente_in)
    return cliente


@router.get(
    "/",
    response_model=List[schema.ClienteOut],
)
def listar_clientes(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    clientes = crud.get_clientes(db, skip=skip, limit=limit)
    return clientes  


@router.get(
    "/{cliente_id}",
    response_model=schema.ClienteOut,
)
def buscar_cliente(
    cliente_id: int,
    db: Session = Depends(get_db),
):
    cliente = crud.get_cliente(db, cliente_id)
    if not cliente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente não encontrado")
    return cliente


@router.put(
    "/{cliente_id}",
    response_model=schema.ClienteOut,
)
def atualizar_cliente(
    cliente_id: int,
    cliente_in: schema.ClienteUpdate,
    db: Session = Depends(get_db),
):
    cliente = crud.update_cliente(db, cliente_id, cliente_in)
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado.",
        )
    return cliente


@router.delete(
    "/{cliente_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def deletar_cliente(
    cliente_id: int,
    db: Session = Depends(get_db),
):
    sucesso = crud.delete_cliente(db, cliente_id)
    if not sucesso:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado.",
        )
    # 204 não retorna corpo
    return None