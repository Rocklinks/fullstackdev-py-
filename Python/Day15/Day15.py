class LibraryItem:
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
    
    def display_info(self):
        return f"ID: {self.item_id}, Title: {self.title}, Author: {self.author}"

class Book(LibraryItem):
    def __init__(self, title, author, item_id, genre):
        super().__init__(title, author, item_id)
        self.genre = genre
    
    def display_info(self):
        return f"ID: {self.item_id}, Title: {self.title}, Author: {self.author}, Genre: {self.genre}"

class Magazine(LibraryItem):
    def __init__(self, title, author, item_id, issue_number):
        super().__init__(title, author, item_id)
        self.issue_number = issue_number
    
    def display_info(self):
        return f"ID: {self.item_id}, Title: {self.title}, Author: {self.author}, Issue Number: {self.issue_number}"

# Example Usage
book1 = Book("1984", "George Orwell", 101, "Dystopian")
magazine1 = Magazine("National Geographic", "Editorial Team", 202, 45)

print(book1.display_info())
print(magazine1.display_info())


class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.__balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. New balance: {self.__balance}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew {amount}. New balance: {self.__balance}"
        return "Insufficient funds or invalid amount"
    
    def get_balance(self):
        return f"Current balance: {self.__balance}"

class SavingsAccount(BankAccount):
    def __init__(self, account_number, initial_balance=0, interest_rate=0.02):
        super().__init__(account_number, initial_balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self.__balance * self.interest_rate
        self.deposit(interest)
        return f"Applied interest: {interest}. New balance: {self.__balance}"


account = SavingsAccount("12345678", 1000, 0.03)
print(account.deposit(500))
print(account.withdraw(200))
print(account.get_balance())
