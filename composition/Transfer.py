from composition.User import User

class Transfer:
    def __init__(self):
        self.banksList = [
            "Meezan Bank",
            "Bank Al Habib",
            "Easypaisa",
            "Jazzcash",
            "Sadapay",
            "MCB",
            "Bank Alfalah",
            "Bank Dubai Islami",
            "Habib bank",
            "Habib Metro",
            "Zarai tarakiyati bank",
            "National Bank"
        ]
        
    def transferFromAccount(self,user):
        exitForOnlineTransfer="key"
        while exitForOnlineTransfer != "X":
            print("___online transfer___")
            userSelectedBankNo = self._getBeneficiaryAccountBank()
            exitForOnlineTransfer = "X"
            if (userSelectedBankNo is not None):
                userAccountNo = input("Please enter your account no (XXX-XXXXX) \n")
                userSelectBank = self.banksList[userSelectedBankNo - 1]
                beneficiaryUser = self._getBeneficiaryUserFromExistingList(userAccountNo, userSelectBank)
                if beneficiaryUser != {}:
                    print("account title =>",beneficiaryUser["account_title"])
                    print("what amount you want to transfer ",beneficiaryUser["account_title"])
                    exitForAmount="key"
                    while exitForAmount!= "X":          
                        amount=self._getAmountFromUser()
                        if (self._isUserAccountBalanceGreaterThanAmount(user, amount)):
                            self._subtractUserAccountBalanceByAmount(user, amount)
                            balance=user["account_balance"]
                            print("your transaction has been successfully completed")
                            print(amount," has been transfer to ",beneficiaryUser["account_title"])
                            print("your current account balance is ",balance,"thanks! for using bank")
                            self._addAmountInUserAccountBalance(beneficiaryUser, amount)
                            exitForAmount="X"
                            exitForOnlineTransfer="X"
                        else:
                            print("insufficient fund in user account.\n user only can transfer amount under ",user["account_balance"])
                            exitForAmount=input("enter X for exit or any key to go back")
                else:
                    print("invalid user or bank")
                    exitForOnlineTransfer=input("press X for exit or any key to go back")
    
    def _getBeneficiaryAccountBank(self):
        exitForAccountBank = "key"
        while (exitForAccountBank != "X"):
            for bankListIndex in range(len(self.banksList)):
                print(bankListIndex + 1 , self.banksList[bankListIndex])
            userSelectedBankNo = int(input("Please select your bank from the list \n"))
            if (userSelectedBankNo < 0 or userSelectedBankNo >= len(self.banksList)):
                print("Invalid bank no! \n")
                userSelectedBankNo = None
                exitForAccountBank = input("Press any key to continue or X to exit\n ")
            else:
                exitForAccountBank = "X"
        return userSelectedBankNo
    
    def _getBeneficiaryUserFromExistingList(self, userAccountNo, userSelectBank):
        user = User()
        beneficiaryUser = user.geUserFromUserListByUserAccount(userAccountNo)
        if (beneficiaryUser != {} and beneficiaryUser["account_bank"] == userSelectBank):
            return beneficiaryUser
        else:
            return {}
    
    def _getAmountFromUser(self):
        amount=int(input("Enter amount \n =>"))
        return amount 
    
    def _isUserAccountBalanceGreaterThanAmount(self, user, amount):
        if (user["account_balance"] >= amount):
            return True
        else:
            return False
    
    def _addAmountInUserAccountBalance (self,user,amount):
        user["account_balance"]+=amount
        
    def _subtractUserAccountBalanceByAmount(self,user, amount):
        user["account_balance"] = user["account_balance"] - amount
