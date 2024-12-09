import sys
def main():
  print('Welcome')
  screening()

def screening():
  print('Welcome to Derine\'s finance tracker. \nPlease state the nature of your transaction. \n1:Income \n2:Expense')
  type = input()
  try:
    int(type)
  except:
    print('Invalid Choice. App Terminated.')
    sys.exit()
  print('What category is this? \n1: Personal \n2: Family \n3: Gifts')
  category = input()
  try:
    int(category)
  except:
    print('Invalid Choice. App Terminated.')
    sys.exit()

main()