from src.lib.Entities.Account import Account
from src.lib.Repositories.TransactionRepository import TransactionRepository


class TransactionService:

    def __init__(self):
        self.__transactionRepository = TransactionRepository()

    def refreshTransactions(self, transactionRecords: list) -> None:
        transactionIds = [transaction[Account.ID_COLUMN] for transaction in transactionRecords]
        existingIds = self.__transactionRepository.getExistingIds(transactionIds)

        recordsToUpdate = filter(lambda transaction: transaction[Account.ID_COLUMN] in existingIds, transactionRecords)
        recordsToCreate = filter(lambda transaction: transaction[Account.ID_COLUMN] not in existingIds, transactionRecords)
        self.__transactionRepository.updateMany(list(recordsToUpdate))
        self.__transactionRepository.createMany(list(recordsToCreate))

