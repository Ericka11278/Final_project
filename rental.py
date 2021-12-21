import pandas as pd
import matplotlib.pyplot as plt
"""we are trying to calculate the amount of money the customer has to pay based
on the amount of hours the customer needs it for and the type of materials they 
need

"""
class Materials:
   def __init__(self,stock,price,name):
            self.stock=stock
            self.price_per_hour=price
            self.item_name=name
            inventory = pd.read_csv('inventory.csv')
            print(inventory)

   def user_input(self,ITEMNAME,stock,input_hours, PRICEPERHOUR):
                inventory = pd.read_csv('inventory.csv')
                ITEMNAME=str(input("Please tell us what you would like to rent"))
                print(ITEMNAME)
                if ITEMNAME in inventory=="Goggles"or"Lab Coat"or"Standard Calculator"or"Scientific Calculator"or"Graphing Calculator":
                 input_hours =int(input("How many hours would you like it for?"))
                print(input_hours)
                if stock==0:
                        print("Please make another selection")
                if stock>self.stock:
                        print("Please make another selection we do not have enough in stock")
                if stock==self.stock:
                        cost= {PRICEPERHOUR} * int(input_hours)
                        return f" You have selected {ITEMNAME} this will cost you {cost} thank you for shopping with us"
                else:
                        raise ValueError