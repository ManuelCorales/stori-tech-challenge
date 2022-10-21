import pandas as pd
import os


class Account:

    ID_COLUMN = "Id"
    DATE_COLUMN = "Date"
    TRANSACTION_COLUMN = "Transaction"

    def __init__(self):
        self.__csvData = self.readCSV()

    def readCSV(self) -> pd.DataFrame:
        return pd.read_csv(os.getcwd() + "/account_transactions/account_transactions.csv")

    def getTotalBalance(self) -> float:
        return round(self.__csvData[self.TRANSACTION_COLUMN].sum(), 4)

    def getAverageDebitAmount(self) -> float:
        debitTransactions = self.__csvData.loc[
            self.__csvData[self.TRANSACTION_COLUMN] < 0
        ][self.TRANSACTION_COLUMN]
        return round(debitTransactions.mean(), 4)

    def getAverageCreditAmount(self) -> float:
        __accountTransactions = self.__csvData.loc[
            self.__csvData[self.TRANSACTION_COLUMN] > 0
        ][self.TRANSACTION_COLUMN]
        return round(__accountTransactions.mean(), 4)

    def getNumberOfTransactionsByMonth(self) -> int:
        return self.__csvData["Date"].sum()

    def getTransactionRecords(self) -> list:
        return self.__csvData.to_dict('records')

    def getAmountOfTransactionsByMonth(self) -> dict:
        transactionsPerMonth = {}
        for index, row in self.__csvData.iterrows():
            date = row[self.DATE_COLUMN].split("/")
            month = int(date[0])
            if (transactionsPerMonth.get(month) is None):
                transactionsPerMonth[month] = 1
            else:
                transactionsPerMonth[month] += 1

        transactionsPerMonth = dict(sorted(transactionsPerMonth.items())) # Dictionary ordered by month
        return transactionsPerMonth
