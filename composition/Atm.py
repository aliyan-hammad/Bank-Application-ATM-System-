from composition.User import User
from composition.Transfer import Transfer

class ATM:
    def atm(self):
        user = User()
        loggedInUser = user.loginIntoAtm()
        if (loggedInUser != {}):
            self.showMenuWithTransactionMenu(loggedInUser)
            
    def showMenuWithTransactionMenu(self,user):
        self.userTransactionMenu(user)
        
    
    def userTransactionMenu(self,user):
        loop2="key"
        while loop2 != "X":
            self.userMenu()
            option=int(input('please select an option'))
            if option == 1:
                self.withDraw(user)
                loop2="X"
            elif option == 2:
                self.balanceInq(user)
                loop2=input("enter X for exit or any key to go back")
            elif option == 3:
                transfer = Transfer()
                transfer.transferFromAccount(user)
                loop2="X"
            else:
                print("invalid option")
                loop2=input("enter X for exit or any key to go back")
    
    def userMenu(self):
        print('''
            1-Withdraw      2-balance inquiry
            3-Fund transfer     4-Pay bill''')
        
    def withDraw(self,user):
        loop2="key"
        while loop2 != "X":
            print('''Withdraw
                1-500     2-1000
                3-2000     4-5000
                5-10000     6-other amount
                ''')
            options=["",500,1000,2000,5000,10000,"other amount"]
            option=int(input("select your amount."))
            if option <= len(options)-2 and option > 0:
                amount=options[option]
                if self.isUserAccountBalanceGreaterThanAmount(user,amount):
                    self.subtractUserAccountBalanceByAmount(user,amount)
                    print(amount," has been deducted from your account")
                    print("take your money below. \n thanks for using this ATM.\n exit your card please..")
                    loop2="X"
                else:
                    print("insufficient fund")
                    loop2="X"
            elif option == len(options)-1:
                print("you wanna other amount")
                userInputAmount=int(input("please enter your amount\n==>"))
                if self.isUserAccountBalanceGreaterThanAmount(user,userInputAmount):
                    self.subtractUserAccountBalanceByAmount(user,userInputAmount)
                    print(userInputAmount," has been deducted from your account")
                    print("thanks for using this ATM.\n please exit your card..")
                    loop2="X"
                elif userInputAmount > user["account_balance"]:
                    print("invalid amount\n please enter an amount b/w 500-",user["account_balance"])
                    loop2=input("enter X for exit or any key to continue")
            else:
                print("invalid option")
                loop2=input("enter X for exit or any key to continue")
         
    def balanceInq(self,user):
        balance=user["account_balance"]
        print("your acount balance is " ,balance)
        
    def isUserAccountBalanceGreaterThanAmount(self, user, amount):
        if (user["account_balance"] >= amount):
            return True
        else:
            return 
    
    def subtractUserAccountBalanceByAmount(self,user, amount):
        user["account_balance"] = user["account_balance"] - amount