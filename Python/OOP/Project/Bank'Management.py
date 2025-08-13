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
    database = 'data.json'

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
        return "".join(alpha + num)


    def createaccount(self):
        info = {
            "name" : input("Tell your name :"),
            "age"  :int(input("Tell your age : ")),
            "E-mail" : input("Tell your E-mail : "),
            "Pin" : int(input("Tell your Pin : ")),
            "Account_no" : 1234,
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
            Bank.__update()









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