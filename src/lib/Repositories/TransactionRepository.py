from src.lib.Repositories.RepositoryDatabase.TransactionRepositoryDatabase import TransactionRepositoryDatabase


class TransactionRepository:

    def __init__(self) -> None:
        self.__dbGateway = TransactionRepositoryDatabase()

    def getExistingIds(self, transactionIds: list) -> None:
        return self.__dbGateway.getExistingIds(transactionIds)

    def createMany(self, transactionRecords: list) -> None:
        self.__dbGateway.createMany(transactionRecords)

    def updateMany(self, transactionRecords: list) -> None:
        self.__dbGateway.updateMany(transactionRecords)
