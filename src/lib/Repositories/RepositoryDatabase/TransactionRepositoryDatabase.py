from src.lib.Entities.TransactionType import TransactionType
from src.lib.Entities.Account import Account
from src.lib.Repositories.RepositoryDatabase.DatabaseConnection import DatabaseConnection

class TransactionRepositoryDatabase:

    __TABLE = 'transactions'

    def __init__(self):
        self.__dbConnection = DatabaseConnection()

    def getExistingIds(self, transactionIds: list) -> list:
        stringForInjection = "".join(['?, ' for i in range(len(transactionIds) - 1)])
        # String of '? ' according to amount of ids

        result = self.__dbConnection.select(f"""
            SELECT id FROM {self.__TABLE}
            WHERE id IN ({stringForInjection}?)
        """, tuple(transactionIds))
        
        existingIds = []
        for row in result:
            existingIds.append(row['id'])
        return existingIds


    def createMany(self, transactionRecords: list) -> None:
        self.__dbConnection.insertMultipleRows(f"""
            INSERT INTO {self.__TABLE}
                (id, account_id, date, transaction_type_id, amount)
            VALUES
                (?, ?, ?, ?, ?)
            """,
            self.__parseTransactionsForCreating(transactionRecords)
        )

    def __parseTransactionsForCreating(self, transactionRecords: list) -> list:
        def mapping(transaction):
            return (
                transaction[Account.ID_COLUMN],
                1, # Hardcode the only account id in the db
                transaction[Account.DATE_COLUMN],
                TransactionType.getCreditType().getId() if transaction[Account.TRANSACTION_COLUMN] > 0 else TransactionType.getDebitType().getId(),
                abs(transaction[Account.TRANSACTION_COLUMN])
            )
        return map(mapping, transactionRecords)

    def updateMany(self, transactionRecords: list) -> None:
        self.__dbConnection.updateMultipleRows(f"""
            UPDATE {self.__TABLE}
            SET
                date = ? ,
                transaction_type_id = ?,
                amount = ? 
            WHERE
                id = ?
            """,
            self.__parseTransactionsForUpdating(transactionRecords)
        )

    def __parseTransactionsForUpdating(self, transactionRecords: list) -> list:
        def mapping(transaction):
            return (
                transaction[Account.DATE_COLUMN],
                TransactionType.getCreditType().getId() if transaction[Account.TRANSACTION_COLUMN] > 0 else TransactionType.getDebitType().getId(),
                abs(transaction[Account.TRANSACTION_COLUMN]),
                transaction[Account.ID_COLUMN]
            )
        return map(mapping, transactionRecords)
            