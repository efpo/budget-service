from sqlalchemy.orm import Session

from . import models


def get_transaction(db: Session, id: int):
    return db.query(models.Transaction).filter(models.transaction.id == id).first()


#def get_transactions_by_name(db: Session, email: str):
#    return db.query(models.User).filter(models.User.email == email).first()

def get_transactions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Transaction).offset(skip).limit(limit).all()


def create_transaction(db: Session, transaction):

    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction