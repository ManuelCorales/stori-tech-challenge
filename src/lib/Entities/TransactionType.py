

class TransactionType:

    __DEBIT_TYPE_ID = 1
    __CREDIT_TYPE_ID = 2

    def __init__(self, data):
        self.__id = data["id"]

    @staticmethod
    def getDebitType():
        data = {"id": TransactionType.__DEBIT_TYPE_ID}
        return TransactionType(data)

    @staticmethod
    def getCreditType():
        data = {"id": TransactionType.__CREDIT_TYPE_ID}
        return TransactionType(data)

    def getId(self):
        return self.__id
