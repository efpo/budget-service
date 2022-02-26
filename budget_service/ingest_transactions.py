#import database.crud
import locale
import pandas as pd


class IngestTransactions():

    def ingest_transactions_from_csv_to_panda(csv_files):
        for file in csv_files:
            df = pd.read_csv(rf'/mnt/c/Users/ekloc/code/budget-service/csv_files/{file}', sep=';', decimal=',')
            print(df)
        return df

    def change_panda_columns_to_english(df):
        df.rename(columns={
            'Bokföringsdag': 'date',
            'Belopp': 'amount',
            'Avsändare': 'sender',
            'Mottagare': 'receiver',
            'Namn': 'name',
            'Rubrik': 'title',
            'Saldo': 'balance',
            'Valuta': 'currency',

        }, inplace=True)
        print(df)
        print(type(df['amount'][0]))
        return df

    def add_transactions_to_database(transactions):
        print('Add tramsactions to database')
