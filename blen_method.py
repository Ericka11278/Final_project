import pandas as pd
import matplotlib.pyplot as plt

def displayinventory():
  """This prompts the potential renter to choose how they would like the inventory
  presented to them.
  Args:
    prompt (str): questions the user how they would like the inventory displayed
    to them
    inventory (csv): 
  """
  while True:
    try:
      prompt = input('How would you like inventory to be displayed? (Graph or Table)')
    except:
      if prompt.lower() == 'graph':
        inventory = pd.read_csv('inventory.csv')
        plt.bar(x=inventory['ITEM NAME'], height=inventory['STOCK'])
        plt.title('Inventory Display')
        plt.xlabel('ITEM NAMES')
        plt.ylabel('STOCK')
        plt.show()
        break
      elif prompt.lower() == 'table':
        inventory = pd.read_csv('inventory.csv')
        print(inventory)
      else:
        print('Wrong input, try Graph or Table')
