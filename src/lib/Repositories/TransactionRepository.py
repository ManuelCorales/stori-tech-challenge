from src.lib.Repositories.RepositoryDatabase.TransactionRepositoryDatabase import TransactionRepositoryDatabase


class TransactionRepository:

    def __init__(self) -> None:
        self.__dbGateway = TransactionRepositoryDatabase()

    def updateTransactions(self, transactionRecords: list) -> None:
        self.__dbGateway.updateTransactions(transactionRecords)
