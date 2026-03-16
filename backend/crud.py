from sqlalchemy.orm import Session

from backend import models, schema


def get_cliente(db: Session, cliente_id: int) -> models.Cliente | None:
    return db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()


def get_cliente_by_email(db: Session, email: str) -> models.Cliente | None:
    return db.query(models.Cliente).filter(models.Cliente.email == email).first()


def get_clientes(db: Session, skip: int = 0, limit: int = 100) -> list[models.Cliente]:
    return (
        db.query(models.Cliente)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_cliente(db: Session, cliente_in: schema.ClienteCreate) -> models.Cliente:
    db_cliente = models.Cliente(
        nome=cliente_in.nome,
        email=cliente_in.email,
        telefone=cliente_in.telefone,
        endereco=cliente_in.endereco,
    )
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente


def update_cliente(
    db: Session,
    cliente_id: int,
    cliente_in: schema.ClienteUpdate,
) -> models.Cliente | None:
    db_cliente = get_cliente(db, cliente_id)
    if not db_cliente:
        return None

    update_data = cliente_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_cliente, field, value)

    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente


def delete_cliente(db: Session, cliente_id: int) -> bool:
    db_cliente = get_cliente(db, cliente_id)
    if not db_cliente:
        return False

    db.delete(db_cliente)
    db.commit()
    return True