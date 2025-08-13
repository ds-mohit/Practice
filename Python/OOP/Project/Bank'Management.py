## create a bank account
## deposit money
## withdraw money
## details
## update details
## delete account

import json
import random
import string
from pathlib import Path
class Bank:
    data = []
    ##database = 'data.json' --> this will work on main directory
    ## this will work on sub directory
    BASE_DIR = Path(__file__).resolve().parent  # Folder where script is located
    database = BASE_DIR / 'data.json'


    try:
        if Path(database).exists():
            with open(database, 'r') as fs:
               data = json.loads(fs.read())
        
        else:
            print("File does not exist")

    except Exception as e:
        print(f"An error occurred: {e}")

    @staticmethod
    def __update(data):
        try:
            with open(Bank.database, 'w') as fs:
                fs.write(json.dumps(Bank.data))
        except Exception as e:
            print(f"An error occurred: {e}")
    
    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k=3)
        spchar = random.choices("!@#$%^&*" , k =1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)


    def createaccount(self):
        info = {
            "name" : input("Tell your name :"),
            "age"  :int(input("Tell your age : ")),
            "E-mail" : input("Tell your E-mail : "),
            "Pin" : int(input("Tell your Pin : ")),
            "Account_no" : Bank.__accountgenerate(),
            "Balance" : 0
        }

        if info['age']<18 or len(str(info['Pin']))<4:
            print("You are not eligible to open an account")
        else:
            print("Account created successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note down your account no.")

            Bank.data.append(info)
            Bank.__update(Bank.data)

    def depositmoney(self):
        account_no = input("Please enter your account no : ")
        pin = int(input("Please enter your pin also : "))

        userdata = [i for i in Bank.data if i['Account_no'] == account_no and i['Pin'] == pin]

        if not userdata:
            print("Account not found")

        else:
            amount = int(input("Please enter the amount you want to deposit : "))
            if amount > 10000 or amount < 0:
                print("Please enter the valid amount")
            else:
                userdata[0]['Balance'] += amount
                Bank.__update(Bank.data)
                print("Money deposited successfully")

    def withdrawmoney(self):
        account_no = input("Please enter your account no : ")
        pin = int(input("Please enter your pin also : "))

        userdata = [i for i in Bank.data if i['Account_no'] == account_no and i['Pin'] == pin]

        if not userdata:
            print("Account not found")

        else:
            amount = int(input("Please enter the amount you want to withdraw : "))
            if amount > userdata[0]['Balance'] or amount < 0:
                print("Please enter the valid amount")
            else:
                userdata[0]['Balance'] -= amount
                Bank.__update(Bank.data)
                print("Money withdrawn successfully")
           
    def accountdetails(self):
        account_no = input("Please enter your account no : ")
        pin = int(input("Please enter your pin also : "))

        userdata = [i for i in Bank.data if i['Account_no'] == account_no and i['Pin'] == pin]

        if not userdata:
            print("Account not found")

        else:
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")

    def updatedetails(self):
        account_no = input("Please enter your account no : ")
        pin = int(input("Please enter your pin also : "))

        userdata = [i for i in Bank.data if i['Account_no'] == account_no and i['Pin'] == pin]

        if not userdata:
            print("Account not found")

        else:
            userdata[0]['name'] = input("Please enter your name : ")
            userdata[0]['age'] = int(input("Please enter your age : "))
            userdata[0]['E-mail'] = input("Please enter your E-mail : ")
            userdata[0]['Pin'] = int(input("Please enter your Pin : "))
            Bank.__update(Bank.data)
            print("Account details updated successfully")

    def deleteaccount(self):
        account_no = input("Please enter your account no : ")
        pin = int(input("Please enter your pin also : "))

        userdata = [i for i in Bank.data if i['Account_no'] == account_no and i['Pin'] == pin]

        if not userdata:
            print("Account not found")

        else:
            Bank.data.remove(userdata[0])
            Bank.__update(Bank.data)
            print("Account deleted successfully")


user = Bank()
print("Press 1 for creating an account")
print("Press 2 for depositing the money in the Bank")
print("Press 3 for withdrawing the money ")
print("Press 4 for account details")
print("Press 5 for updating account details")
print("Press 6 for deleting your account")

check=int(input("Please tell your response:"))

if check == 1:
    user.createaccount()

if check ==2:
    user.depositmoney()

if check ==3:
    user.withdrawmoney()

if check ==4:
    user.accountdetails()

if check ==5:
    user.updatedetails()

if check ==6:
    user.deleteaccount()