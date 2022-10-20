from src.lib.Entities.TransactionType import TransactionType
from src.lib.Entities.Account import Account
from src.lib.Repositories.RepositoryDatabase.DatabaseConnection import DatabaseConnection

class TransactionRepositoryDatabase:

    def __init__(self):
        self.__dbConnection = DatabaseConnection()

    def updateTransactions(self, transactionRecords: list) -> None:
        self.__dbConnection.updateMultipleRows(f"""
            UPDATE transactions
            SET
                date = ? ,
                amount = ? ,
                transaction_type_id = ?
            WHERE
                id = ?
            """,
            self.__parseTransactionData(transactionRecords)
        )

    def __parseTransactionData(self, transactionRecords: list) -> list:
        def mappingFunction(transaction):
            return (
                transaction[Account.DATE_COLUMN],
                abs(transaction[Account.TRANSACTION_COLUMN]),
                TransactionType.getCreditType().getId() if transaction[Account.TRANSACTION_COLUMN] > 0 else TransactionType.getDebitType().getId(),
                transaction[Account.ID_COLUMN]
            )
        return map(mappingFunction, transactionRecords)
            