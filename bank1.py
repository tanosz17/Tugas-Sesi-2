# Sultan Nurfalah
# TI23H
class BankAccount:
  def __init__(self, owner_name, balance):
      self.owner_name = owner_name
      self.balance = balance
  
  def deposit(self, amount):
      self.balance = self.balance + amount
      print("Deposit :", amount, " - Your balance is", self.balance)
      
  def withdraw(self, amount):
      self.balance = self.balance - amount
      print("withdraw :", amount, " - Your balance is", self.balance)
      
  def check_balance(self):
      print('Your balance is: ', self.balance)
      
account1 = BankAccount('Ikhsan', 10000)
account1.check_balance()
account1.deposit(5000)
account1.withdraw(10000)
