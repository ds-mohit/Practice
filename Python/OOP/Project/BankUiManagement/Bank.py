import json
import random
import string
from pathlib import Path

class Bank:
    BASE_DIR = Path(__file__).resolve().parent
    database = BASE_DIR / 'data.json'

    def __init__(self):
        self.data = []
        self.load_data()

    def load_data(self):
        if self.database.exists():
            try:
                with open(self.database, 'r') as fs:
                    self.data = json.load(fs)
            except json.JSONDecodeError:
                self.data = []
        else:
            self.data = []
            self.save_data()

    def save_data(self):
        with open(self.database, 'w') as fs:
            json.dump(self.data, fs, indent=4)

    @staticmethod
    def _generate_account_no():
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        acc = alpha + num + spchar
        random.shuffle(acc)
        return "".join(acc)

    def create_account(self, name, age, email, pin):
        if age < 18 or len(str(pin)) < 4:
            return False, "You are not eligible to open an account"

        new_account = {
            "name": name,
            "age": age,
            "E-mail": email,
            "Pin": pin,
            "Account_no": self._generate_account_no(),
            "Balance": 0
        }
        self.data.append(new_account)
        self.save_data()
        return True, new_account

    def deposit(self, account_no, pin, amount):
        user = self._find_user(account_no, pin)
        if not user:
            return False, "Account not found"
        if amount <= 0 or amount > 10000:
            return False, "Invalid deposit amount"
        user["Balance"] += amount
        self.save_data()
        return True, f"₹{amount} deposited successfully"

    def withdraw(self, account_no, pin, amount):
        user = self._find_user(account_no, pin)
        if not user:
            return False, "Account not found"
        if amount <= 0 or amount > user["Balance"]:
            return False, "Invalid withdrawal amount"
        user["Balance"] -= amount
        self.save_data()
        return True, f"₹{amount} withdrawn successfully"

    def get_details(self, account_no, pin):
        user = self._find_user(account_no, pin)
        if not user:
            return False, "Account not found"
        return True, user

    def update_details(self, account_no, pin, name=None, email=None, new_pin=None):
        user = self._find_user(account_no, pin)
        if not user:
            return False, "Account not found"
        if name:
            user["name"] = name
        if email:
            user["E-mail"] = email
        if new_pin:
            user["Pin"] = new_pin
        self.save_data()
        return True, "Details updated successfully"

    def delete_account(self, account_no, pin):
        user = self._find_user(account_no, pin)
        if not user:
            return False, "Account not found"
        self.data.remove(user)
        self.save_data()
        return True, "Account deleted successfully"

    def _find_user(self, account_no, pin):
        for user in self.data:
            if user["Account_no"] == account_no and user["Pin"] == pin:
                return user
        return None
