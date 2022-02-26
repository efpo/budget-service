from budget_service.database.crud import create_transaction
from ingest_transactions import IngestTransactions
from sqlalchemy import create_engine
from database.database import engine
from database import models
from database.main import get_db

csv_files = [
        'PERSONKONTO32690103745-2022.01.0215.24.csv',
        'PERSONKONTO890326-1439-2022.01.2820.41.csv'
    ]


df = IngestTransactions.ingest_transactions_from_csv_to_panda(csv_files)
df = IngestTransactions.change_panda_columns_to_english(df)

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
    create_transaction(db=get_db(), transaction=transaction)
