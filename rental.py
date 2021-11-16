"""we are trying to calculate the amount of money the customer has to pay based
on the amount of hours the customer needs it for and the type of materials they 
need

"""
class Materials:
    """
    This class gives us the opportunity to run the calculations of the user's 
    request and returns their cost
    """
    def __init__(self,stock,price,name):
        """
instantiating what we have 
Args:
Stock(int) this shows what we have as a whole in inventory
price(int) this is the price of the corresponding materials
name(str) this is the name of the materials we have 
        """
        self.stock = stock
        self.price_per_hour=price
        self.item_name=name
    def user_input(self,input_name,input_stock,input_hours, price_per_hour):
        """
here we are seeing what the calculation is based on the user response
Args:
input_name(str) this is the name of the material the user wants 
input_stock(int)this is what we currently have in stock
input_hours(int)this is the hours the user wants to rent it for
price_per_hour(int)this is the price the user will have to pay per hour
        """
        input_name=input("Please tell us what you would like to rent")
        print (input_name)
        input_hours=input("How many hours would you like it for?")
        print(input_hours)
        if input_stock == 0:
            raise ValueError and print ("Please make another selection")
        if input_stock<self.stock:
            raise ValueError and print ("Please make another selection")
        if input_stock<=self.stock:
            cost= int(price_per_hour) * int(input_hours)
            return f" You have selected {input_name} this will cost you {cost} thank you for shopping with us"


     


