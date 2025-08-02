class User:
    def __init__(self):
        self.users=[
        { 
         "account_no":"111-12345",
         "account_bank": "Meezan Bank",
            "account_title":"Aliyan hamad",
            "account_password":54321,
            "account_balance":5000,
            },
        { "account_no":"112-67890",
         "account_bank": "Bank Al Habib",
            "account_title":"Muhammad Shariq",
            "account_password": 19876,
            "account_balance": 5000,
            },
        { "account_no":"113-19876",
         "account_bank": "MCB",
            "account_title":"Abdul Bari",
            "account_password": 67890,
            "account_balance": 5000,
            },
        { "account_no":"114-54321",
         "account_bank": "Habib Metro",
            "account_title":"Akbar Ali",
            "account_password":12345,
            "account_balance": 5000,
            },
        { "account_no":"115-24680",
         "account_bank": "Meezan Bank",
            "account_title":"Farzain Ali",
            "account_password": 18642,
            "account_balance": 5000,
            }
        ]
    
    def geUserFromUserListByUserAccount(self, userAccountNo):
        user={}
        for existingUser in self.users:
            if (existingUser["account_no"] == userAccountNo):
                user = existingUser
                break
        return user
    
    def loginIntoAtm(self):
        exitForLogin = "key"
        loggedInUser = {}
        while exitForLogin != "X":
            cardNo=self.askCardFromUser()
            if cardNo < len(self.users):
                user=self.users[cardNo]
                print("welcome ",user["account_title"])
                loginAttempt = 0
                while loginAttempt != 3: 
                    password=int(input("please enter your 5 digit pin\n==>"))
                    if password == user["account_password"]:
                        loggedInUser = user
                        exitForLogin = 'X'
                        loginAttempt=3
                    else:
                        print("invalid user or password")
                        loginAttempt+=1
                        if loginAttempt == 3:
                            print("sorry you have tried too much \n exit your card please")      
            else:
                print("invalid card or user")
        
        return loggedInUser
    
    def askCardFromUser(self):
        userNo=int(input("insert your card please.."))
        return userNo
        
    def logInForBank(self):
        user1InputAccountNo = input("enter the account number: \n")
        loggedInUser = {}
        
        for existingUser in self.users:
            if (existingUser["account_no"] == user1InputAccountNo):
                loggedInUser = existingUser
        return loggedInUser
                
                
    def profileOfLoggedInUser(self,user):
        print(f'''Welcome to {user["account_bank"]        }
            Account number => {user["account_no"]}
            Account title => {user["account_title"]}
            Account balance => {user["account_balance"]}''')
