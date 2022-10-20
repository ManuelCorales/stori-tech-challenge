from src.lib.Entities.Account import Account
from email.message import EmailMessage
import calendar
import smtplib


class EmailService:
    EMAIL_ADDRESS = 'mcoralesdev@gmail.com'
    EMAIL_PASSWORD = 'jjsysibprguoxrwa'

    def __init__(self):
        pass

    def sendAccountDataEmail(self, toEmail: str, accountData: Account) -> None:
        message = EmailMessage()
        self.configureMessage(toEmail, message)
        self.setMessageBody(message, accountData)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.EMAIL_ADDRESS, self.EMAIL_PASSWORD)
            smtp.send_message(message)
            print("Email sent to " + toEmail)

    def configureMessage(self, toEmail: str, message: EmailMessage) -> None:
        message['Subject'] = 'Tech challenge'
        message['From'] = self.EMAIL_ADDRESS
        message['To'] = toEmail

    def setMessageBody(self, message: EmailMessage, accountData: Account) -> None:
        """Builds HTML email body"""
        message.set_content(f'''
            <!DOCTYPE html>
            <html>
                <body style="font-family: sans-serif">
                    <div style="background-color:#eee;padding:10px 20px;">
                        <h1 style="color#454349;">
                            Tech challenge: this is the summary of your account
                        </h1>
                    </div>
                    <div style="padding:20px 0px; font-size: 15px">
                        <div>
                            <table style="display: inline-flex">
                                <tr><b>Total balance is {accountData.getTotalBalance()} </b></tr>
                                {self.__getTransactionsPerMonthRows(accountData)}
                            </table>
                            <table style="display: inline-flex; padding-left: 30px">
                                <tr>Average debit amount: {accountData.getAverageDebitAmount()}</tr>
                                <tr>Average credit amount: {accountData.getAverageCreditAmount()}</tr>
                            </table>                                    
                        </div>
                        <img src="https://blog.storicard.com/wp-content/uploads/2019/07/Stori-horizontal-11.jpg" style="height: 100px;">
                    </div>
                </body>
            </html>
            ''', subtype='html')

    def __getTransactionsPerMonthRows(self, accountData: Account) -> str:
        """Returns a string of the transactions per month to insert into html body"""
        transactionsPerMonth = accountData.getAmountOfTransactionsByMonth()
        rows = ""
        for monthNumber in transactionsPerMonth:
            monthName = calendar.month_name[monthNumber]
            rows += f"""<tr> Number of transactions in {monthName}: {transactionsPerMonth[monthNumber]} </tr>"""
        return rows
