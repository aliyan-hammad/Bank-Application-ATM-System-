from composition.Transfer import Transfer
from composition.User import User
from composition.Atm import ATM

class Bank:
    def SelectProcess(self):
        exitTheLoop="key"
        while exitTheLoop != "X":
            select=int(input("please select an option:\nEnter 1 for Banking==>\n Enter 2 for ATM==>\n"))
            if select == 1:
                self.banking()
                # exitTheLoop="X"
            elif select == 2:
                atm = ATM()
                atm.atm()
                # exitTheLoop="X"
            else:
                print("invalid option.")
    def banking(self):
        exitFromBanking="key"
        while exitFromBanking != "X":
            print("Welcome to the bank")
            user=User()
            loggedInUser=user.logInForBank()
            if loggedInUser != {}:
                user.profileOfLoggedInUser(loggedInUser)
                self.getUserToTransactionMenu(loggedInUser)
                exitFromBanking="X"
            else:
                print("invalid user, user does not exist")
                exitFromBanking=input("enter X for exit or any key to continue")
    def getUserToTransactionMenu(self,user):
        loop2="key"
        while loop2 != "X":
            transactionsOptions=["1-With draw","2-Deposit","3-Transfer"]
            for options in transactionsOptions:
                print(options)
            option=int(input("select an option please"))
            if option == 1:
                self.cashWithdraw(user)
                loop2="X"
            elif option == 2:
                self.cashDeposit(user)
                loop2="X"
            elif option == 3:
                transfer = Transfer()
                transfer.transferFromAccount(user)
                loop2="X"
            else:
                print("no more option yet\n try with another option")
                loop2=input("enter X for exit or any key to go back")  
    def cashWithdraw(self,user):
        loop3 = "key"
        while loop3 != "X":
            print("___Cash withdraw___")
            amount = self.getAmountFromUser()
            if (self.isUserAccountBalanceGreaterThanAmount(user, amount)):
                self.subtractUserAccountBalanceByAmount(user, amount)
                print(amount," has been withdraw from your account\nthanks! for using bank your current account balance is ",user["account_balance"])
                loop3="X"
            else:
                print("Insufficient fund.\n You can only withdraw amount under ", user["account_balance"])
                loop3=input("enter X for exit or any key to go back")
    def getAmountFromUser(self):
        amount=int(input("Enter amount \n =>"))
        return amount 
    def isUserAccountBalanceGreaterThanAmount(self, user, amount):
        if (user["account_balance"] >= amount):
            return True
        else:
            return False
    
    def subtractUserAccountBalanceByAmount(self,user, amount):
        user["account_balance"] = user["account_balance"] - amount
                            
    def cashDeposit(self,user):
        print("__Cash deposit__")
        amount=self.getAmountFromUser()
        self.addAmountInUserAccountBalance(user,amount) 
        print(amount," has been deposit in your account\n thanks! for using bank,your current account balance is ",user["account_balance"])
    def addAmountInUserAccountBalance (self,user,amount):
        user["account_balance"]+=amount
    # check account balance
    # if account balance is greater or equal to amount
    # then return true
    # otherwise show error message & return false

bank=Bank()
bank.SelectProcess()


