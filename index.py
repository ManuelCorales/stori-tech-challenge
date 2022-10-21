import sys
import os
import re
from src.lib.Services.Transaction.TransactionService import TransactionService
from src.lib.Services.Emailing.EmailService import EmailService
from src.lib.Entities.Account import Account
from src.lib.Repositories.RepositoryDatabase.TransactionRepositoryDatabase import TransactionRepositoryDatabase
from src.lib.Repositories.TransactionRepository import TransactionRepository

def validateInput(input: list) -> bool:
    """
        Validates wether the input from console is valid.
        The input must have an email
    """
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (len(sys.argv) < 2 or re.search(regex, input[1]) is None):
        print("Invalid Email")
        quit()

    return True


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__)) # Set root directory

    if (validateInput(sys.argv)):
        emailService = EmailService() # Intantiate email service
        accountData = Account() # Intantiate account
        transactionsRecords = accountData.getTransactionRecords() # Get the account transaction records
        transactionService = TransactionService()
        transactionService.refreshTransactions(transactionsRecords) # Update transactions from database according to the ones of the csv
        emailService.sendAccountDataEmail(sys.argv[1], accountData) # Finally send email
