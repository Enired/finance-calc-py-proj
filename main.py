import sys
from datetime import datetime
def main():
  print('Welcome')
  screening()

class Transaction:

  def __init__(self, type, amount, category, month):
    self.set_type(type)
    self.set_amount(amount)
    self.set_category(category)
    self.set_month(month)

  def get_type(self):
    return self.type

  def get_amount(self):
    return self.amount
  
  def get_category(self):
    return self.category
  
  def get_month(self):
    return self.month

  def set_type(self, type):
    self.type = type
    return

  def set_amount(self, amount):
    self.amount = amount
    return
    
  def set_category(self, category):
    self.category = category
    return

  def set_month(self, month):
    self.month = month
    return





def screening():
  print('Welcome to Derine\'s finance tracker. \nPlease state the nature of your transaction. \n1:Income \n2:Expense')
  choice = input()
  type = ''
  category = ''
  try:
    match choice:
      case '1':
        type = 'Income'
        print('hello')
      case '2':
        type = 'Expense'
        print('world')
  except:
    print('Invalid Choice. App Terminated.')
    sys.exit()
  print('What ategory is this? \n1: Personal \n2: Family \n3: Gifts')
  choice = input()
  try:
    match choice:
      case '1':
        category = 'Personal'
      case '2':
        category = 'Family'
      case '3':
        category = 'Gifts'
  except:
    print('Invalid Choice. App Terminated.')
    sys.exit()

  current_month = datetime.now().month
  test = Transaction(type, category, current_month)
  return

main()