#Jay Mathur INST 326 Final Project
# Main()code

def main():
    
    #Instantiate the class for the lab rental shop and the customer
    
    shop = Labrental("initial coat, goggle, and calculator stock")
    
    customer = Customer()
    
    #Start the program with the options for renting coats, goggles, and 
    #calculators.
    
    #Use a while loop to offer the options for the program
    
    while True:
        print("""
        ------Lab Supply Rental Shop-------------
        1. Display available stock of items
        2. Rent lab coat on hourly basis $2
        3. Rent lab coat on daily basis $8
        4. Rent lab coat on weekly basis $20
        5. Return lab coat
        6. Rent goggles on hourly basis $2
        7. Rent goggles on daily basis $8
        8. Rent goggles on weekly basis $20
        9. Return goggles
        10. Rent calculator on hourly basis $5
        11. Rent calculator on daily basis $20
        12. Rent calculator on weekly basis $60
        13. Return calculator
        14. Exit
        """)
        
        
        #Get user choice as an input
        
        choice = input("Enter your choice: ")
        
        #Use if and elif statements to handle the user choices
        
        if choice == 1:
            shop.(use shop class method to display stock)
        
        #This code will be how to handle renting lab coat, goggles, or
        # calculator for the hourly, daily, or weekly methods              
        
        if  choice == 2:
            customer.rentalTime = shop.(method to rent on hourly basis)(customer.(method to request labcoat))
            customer.plannedhours = input("How many hours do you plan to rent for?")
            plannedcost = customer.plannedhours * 2
            print(f"Your estimated rental cost is ${plannedcost}")
            customer.rentalBasis = 1
            
        elif choice == 3:
            customer.rentalTime = shop.(method to rent on daily basis)(customer.(method to request labcoat))
            customer.planneddays = input("How many days do you plan to rent for?")
            plannedcost = customer.planneddays * 8
            print(f"Your estimated rental cost is ${plannedcost}")
            customer.rentalBasis = 2
            
        elif choice == 4:
            customer.rentalTime = shop.(method to rent on weekly basis)(customer.(method to request labcoat))
            customer.plannedweeks = input("How many weeks do you plan to rent for?")
            plannedcost = customer.plannedweeks * 20
            print(f"Your estimated rental cost is ${plannedcost}")
            customer.rentalBasis = 3
        
        elif choice == 5:
            customer.bill = shop.(method to return llabcoat)(customer.(method to return labcoat))
            #Reset the shop and customer attributes after the return
            customer.rentalBasis, customer.rentalTime,customer.labcoat = 0,0,0
            customer.plannedhours, customer.planneddays, customer.plannedweeks = 0,0,0

        elif  choice == 6:
            customer.rentalTime = shop.(method to rent on hourly basis)(customer.(method to request goggles))
            customer.plannedhours = input("How many hours do you plan to rent for?")
            plannedcost = customer.plannedhours * 2
            print(f"Your estimated rental cost is ${plannedcost}")
            customer.rentalBasis = 1
            
        elif choice == 7:
            customer.rentalTime = shop.(method to rent on daily basis)(customer.(method to request goggles))
            customer.planneddays = input("How many days do you plan to rent for?")
            plannedcost = customer.planneddays * 8
            print(f"Your estimated rental cost is ${plannedcost}")
            customer.rentalBasis = 2
            
        elif choice == 8:
            customer.rentalTime = shop.(method to rent on weekly basis)(customer.(method to request goggles))
            customer.plannedweeks = input("How many weeks do you plan to rent for?")
            plannedcost = customer.plannedweeks * 20
            print(f"Your estimated rental cost is ${plannedcost}")
            customer.rentalBasis = 3
        
        elif choice == 9:
            customer.bill = shop.(method to return googles)(customer.(method to return goggles))
            #Reset the shop and customer attributes after the return
            customer.rentalBasis, customer.rentalTime,customer.goggles = 0,0,0
            customer.plannedhours, customer.planneddays, customer.plannedweeks = 0,0,0
        
        elif  choice == 10:
            customer.rentalTime = shop.(method to rent on hourly basis)(customer.(method to request calculator))
            customer.plannedhours = input("How many hours do you plan to rent for?")
            plannedcost = customer.plannedhours * 5
            print(f"Your estimated rental cost is ${plannedcost}")
            customer.rentalBasis = 1
            
        elif choice == 11:
            customer.rentalTime = shop.(method to rent on daily basis)(customer.(method to request calculator))
            customer.planneddays = input("How many days do you plan to rent for?")
            plannedcost = customer.planneddays * 20
            print(f"Your estimated rental cost is ${plannedcost}")
            customer.rentalBasis = 2
            
        elif choice == 12:
            customer.rentalTime = shop.(method to rent on weekly basis)(customer.(method to request calculator))
            customer.plannedweeks = input("How many weeks do you plan to rent for?")
            plannedcost = customer.plannedweeks * 60
            print(f"Your estimated rental cost is ${plannedcost}")
            customer.rentalBasis = 3
        
        elif choice == 13:
            customer.bill = shop.(method to return googles)(customer.(method to return calculator))
            #Reset the shop and customer attributes after the return
            customer.rentalBasis, customer.rentalTime,customer.calculator = 0,0,0
            customer.plannedhours, customer.planneddays, customer.plannedweeks = 0,0,0    
            
        elif choice == 14:
            break
        
            
        
        