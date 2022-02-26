from typing import List
from venv import create
from budget_service.database.database import SessionLocal, engine
from budget_service.ingest_transactions import IngestTransactions

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session


from budget_service.database import crud
from budget_service.database import models
#from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


csv_files = [
        'PERSONKONTO32690103745-2022.01.0215.24.csv',
        'PERSONKONTO890326-1439-2022.01.2820.41.csv'
    ]



#@app.post("/transactions/test")
def create_transaction_():#db: Session = Depends(get_db)):
    df = IngestTransactions.ingest_transactions_from_csv_to_panda(csv_files)
    df = IngestTransactions.change_panda_columns_to_english(df)
    db = SessionLocal()
    for index, row in df.iterrows():
        transaction = models.Transactions(
            date=row['date'], 
            amount=row['amount'],
            sender=row['sender'],
            receiver=row['receiver'],
            name=row['name'],
            title=row['title'],
            balance=row['balance']
        )
        crud.create_transaction(db=db, transaction=transaction)

@app.post("/transactions/")
def create_transaction(transaction, db: Session = Depends(get_db)):
    #db_transaction = crud.get_user_by_email(db, email=user.email)
    #if transaction:
    #    raise HTTPException(status_code=400, detail="Transaction already registered")
    return crud.create_transaction(db=db, transaction=transaction)


@app.get("/transactions/")
def read_transactions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    transactions = crud.get_transactions(db, skip=skip, limit=limit)
    return transactions


@app.get("/transactions/{transaction_id}")
def read_transactions(id: int, db: Session = Depends(get_db)):
    db_transaction = crud.get_transaction(db, id=id)
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return db_transaction


create_transaction_()