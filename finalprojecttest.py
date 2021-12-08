#INST326 Team Project Lab Rental Shop

import datetime

class LabRental:
    
    def __init__(self, goggstock=0, labcoatstock=0, standcalcstock=0,\
        scientcalcstock=0, graphcalcstock=0):
        """
        Our class that instantiates lab rental shop.
        """
        self.goggstock = goggstock
        self.labcoatstock = labcoatstock
        self.standcalcstock = standcalcstock
        self.scientcalcstock = scientcalcstock
        self.graphcalcstock = graphcalcstock
    
    #ERICKA'S 'CODE'
    def displaystock(self):
        """
        Displays the lab items currently available for rent in the shop.
        """
        print(f"We currently have {self.goggstock} goggles available to rent.")
        print(f"We currently have {self.labcoatstock} lab coats available to\
            rent.")
        print(f"We currently have {self.standcalcstock} standard calculators\
            available to rent.")
        print(f"We currently have {self.scientcalcstock} scientific calculators\
            available to rent.")
        print(f"We currently have {self.graphcalcstock} graphing calculators\
            available to rent.")
        
        return (self.goggstock, self.labcoatstock, self.standcalcstock,
                self.scientcalcstock, self.graphcalcstock)

    def rentItemOnHourlyBasis(self, choice, n):
        """
        Rents a lab item on hourly basis to a customer.
        """
        if choice == 2:
            
            if n <= 0:
                print("Number of goggles must be positive!")
                return None
        
            elif n > self.goggstock:
                print("Sorry! We only have {self.goggstock} goggles available\
                    to rent.")
                return None
        
            else:
                now = datetime.datetime.now()                      
                print(f"You have rented {n} goggles on hourly basis today at\
                    {now.hour} hours.")
                print("You will be charged $9 for each hour per set of goggles.")
                print("We hope that you enjoy our service.")

                self.goggstock = self.goggstock - n
                return now
        
        elif choice == 3:
            
            if n <= 0:
                print("Number of lab coats must be positive!")
                return None
        
            elif n > self.labcoatstock:
                print("Sorry! We only have {self.labcoatstock} lab coats\
                available to rent.")
                return None
        
            else:
                now = datetime.datetime.now()                      
                print(f"You have rented {n} lab coats on hourly basis today at\
                    {now.hour} hours.")
                print("You will be charged $25 for each hour per lab coat.")
                print("We hope that you enjoy our service.")

                self.labcoatstock = self.labcoatstock - n
                return now
            
        elif choice == 4:
            
            if n <= 0:
                print("Number of standard calculators must be positive!")
                return None
        
            elif n > self.standcalcstock:
                print("Sorry! We only have {self.standcalcstock} standard\
                    calculators available to rent.")
                return None
        
            else:
                now = datetime.datetime.now()                      
                print(f"You have rented {n} standard calculators on hourly\
                    basis today at {now.hour} hours.")
                print("You will be charged $5 for each hour per standard\
                    calculator.")
                print("We hope that you enjoy our service.")

                self.standcalcstock = self.standcalcstock - n
                return now
            
        elif choice == 5:
            
            if n <= 0:
                print("Number of scientific calculators must be positive!")
                return None
        
            elif n > self.scientcalcstock:
                print("Sorry! We only have {self.scientcalcstock} scientific\
                    calculators available to rent.")
                return None
        
            else:
                now = datetime.datetime.now()                      
                print(f"You have rented {n} scientific calculators on hourly\
                    basis today at {now.hour} hours.")
                print("You will be charged $7 for each hour per scientific\
                    calculator.")
                print("We hope that you enjoy our service.")

                self.scientcalcstock = self.scientcalcstock - n
                return now
            
        elif choice == 6:
            
            if n <= 0:
                print("Number of graphing calculators must be positive!")
                return None
        
            elif n > self.graphcalcstock:
                print("Sorry! We only have {self.graphcalcstock} graphing\
                    calculators available to rent.")
                return None
        
            else:
                now = datetime.datetime.now()                      
                print(f"You have rented {n} graphing calculators on hourly\
                    basis today at {now.hour} hours.")
                print("You will be charged $10 for each hour per graphing\
                    calculator.")
                print("We hope that you enjoy our service.")

                self.graphcalcstock = self.graphcalcstock - n
                return now 
     
    
        
    #JOSEPHINE'S PART OF THE CODE   
    def returnItem(self, choice, request):
        """
        1. Accept a rented item from a customer
        2. Replenishes the inventory
        """
        if choice == 7:
            rentalTime, numofgoggles, planhours = request
            bill = 0

            if rentalTime and numofgoggles:
                self.goggstock = self.goggstock + numofgoggles
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime
        
                # hourly bill calculation
                
                bill = round(rentalPeriod.seconds / 3600) * 9 * numofgoggles
                if round(rentalPeriod.seconds / 3600) > planhours:
                    latehours = (round(rentalPeriod.seconds / 3600) - planhours)
                    latefee = latehours * 2
                    bill = bill + latefee
                    print("Thanks for returning your goggles.")
                    print(f"You returned your goggles late so a late fee of \
                        ${latefee} will be added to your bill.")
                    print(f"Your total bill is ${bill}.")
                    return bill
                
                else:
                    print("Thanks for returning your goggles.")
                    print(f"Your total bill is ${bill}.")
                    return bill
                
                
        elif choice == 8:
            rentalTime, numoflabcoats, planhours = request
            bill = 0

            if rentalTime and numoflabcoats:
                self.labcoatstock = self.labcoatstock + numoflabcoats
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime
        
                # hourly bill calculation
                
                bill = round(rentalPeriod.seconds / 3600) * 25 * numoflabcoats
                if round(rentalPeriod.seconds / 3600) > planhours:
                    latehours = (round(rentalPeriod.seconds / 3600) - planhours)
                    latefee = latehours * 10
                    bill = bill + latefee
                    print("Thanks for returning your labcoats.")
                    print(f"You returned your labcoats late so a late fee of \
                        ${latefee} will be added to your bill.")
                    print(f"Your total bill is ${bill}.")
                    return bill
                
                else:
                    print("Thanks for returning your lab coats.")
                    print(f"Your total bill is ${bill}.")
                    return bill            
                    
                    
        elif choice == 9:
            rentalTime, numofstandcalcs, planhours = request
            bill = 0

            if rentalTime and numofstandcalcs:
                self.standcalcstock = self.standcalcstock + numofstandcalcs
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime
        
                # hourly bill calculation
                
                bill = round(rentalPeriod.seconds / 3600) * 5 * numofstandcalcs
                if round(rentalPeriod.seconds / 3600) > planhours:
                    latehours = (round(rentalPeriod.seconds / 3600) - planhours)
                    latefee = latehours * 2
                    bill = bill + latefee
                    print("Thanks for returning your standard calculators.")
                    print(f"You returned your standard calculators late so a\
                        late fee of ${latefee} will be added to your bill.")
                    print(f"Your total bill is ${bill}.")
                    return bill
                
                else:
                    print("Thanks for returning your standard calculators.")
                    print(f"Your total bill is ${bill}.")
                    return bill
                
                
        elif choice == 10:
            rentalTime, numofscientcalcs, planhours = request
            bill = 0

            if rentalTime and numofscientcalcs:
                self.scientcalcstock = self.scientcalcstock + numofscientcalcs
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime
        
                # hourly bill calculation
                
                bill = round(rentalPeriod.seconds / 3600) * 7 * numofscientcalcs
                if round(rentalPeriod.seconds / 3600) > planhours:
                    latehours = (round(rentalPeriod.seconds / 3600) - planhours)
                    latefee = latehours * 3
                    bill = bill + latefee
                    print("Thanks for returning your scientific calculators.")
                    print(f"You returned your scientific calculators late so a\
                        late fee of ${latefee} will be added to your bill.")
                    print(f"Your total bill is ${bill}.")
                    return bill
                
                else:
                    print("Thanks for returning your scientific calculators.")
                    print(f"Your total bill is ${bill}.")
                    return bill                             
            
            
        elif choice == 11:
            rentalTime, numofgraphcalcs, planhours = request
            bill = 0

            if rentalTime and numofgraphcalcs:
                self.graphcalcstock = self.graphcalcstock + numofgraphcalcs
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime
        
                # hourly bill calculation
                
                bill = round(rentalPeriod.seconds / 3600) * 10 * numofgraphcalcs
                if round(rentalPeriod.seconds / 3600) > planhours:
                    latehours = (round(rentalPeriod.seconds / 3600) - planhours)
                    latefee = latehours * 4
                    bill = bill + latefee
                    print("Thanks for returning your graphing calculators.")
                    print(f"You returned your graphing calculators late so a\
                        late fee of ${latefee} will be added to your bill.")
                    print(f"Your total bill is ${bill}.")
                    return bill
                
                else:
                    print("Thanks for returning your graphing calculators.")
                    print(f"Your total bill is ${bill}.")
                    return bill    
        else:
            print("Are you sure you rented an item with us?")
            return None



class Customer:

    def __init__(self):
        """
        Our constructor method which instantiates various customer objects.
        """
        
        self.goggles = 0
        self.labcoats = 0
        self.standcalc = 0
        self.scientcalc = 0
        self.graphcalc = 0
        self.goggrentalTime = 0
        self.labcoatrentalTime = 0
        self.standcalcrentalTime = 0
        self.scientcalcrentalTime = 0
        self.graphcalcrentalTime = 0
        self.goggplannedhours = 0
        self.labcoatplannedhours = 0
        self.standcalcplannedhours = 0
        self.scientcalcplannedhours = 0
        self.graphcalcplannedhours = 0
        self.bill = 0
        self.name = input("What is your name?")
        self.phone = input("What is your phone number?")
        

    
    def requestItem(self, choice):
        """
        Takes a request from the customer for the number of items to rent.
        """
        
        if choice == 2:
            numgoggles = input("How many googles would you like to rent?")
            numgoggles = int(numgoggles)
            goggplanhours = input("How many hours do you plan to rent for?")
            goggplanhours = int(goggplanhours)
            goggplancost = (goggplanhours) * (9) * (numgoggles)
            print(f"Your estimated cost will be ${goggplancost}.")
            self.goggplannedhours = goggplanhours
            
            try:
                numgoggles = int(numgoggles)
            
            except ValueError:
                print("That is not a positive integer!")
                return -1
            
            if numgoggles < 1:
                print("Invalid input. Number of goggles should be greater\
                    than zero!")
            else:
                self.goggles =  numgoggles
                return self.goggles
            
        
        if choice == 3:
            numlabcoats = input("How many lab coats would you like to rent?")
            labcoatplanhours = input("How many hours do you plan to rent for?")
            labcoatplanhours = int(labcoatplanhours)
            labcoatplancost = (labcoatplanhours) * (25) * (numlabcoats)
            print(f"Your estimated cost will be ${labcoatplancost}.")
            self.labcoatplannedhours = labcoatplanhours
            
            try:
                numlabcoats = int(numlabcoats)
            
            except ValueError:
                print("That is not a positive integer!")
                return -1
            
            if numlabcoats < 1:
                print("Invalid input. Number of lab coats should be greater\
                    than zero!")
            else:
                self.labcoats =  numlabcoats
                return self.labcoats  
            
            
        if choice == 4:
            numstandcalc = input("How many standard calculators would you like\
                to rent?")
            standcalclanhours = input("How many hours do you plan to rent for?")
            standcalcplanhours = int(standcalcplanhours)
            standcalcplancost = (standcalcplanhours)*5*numstandcalc
            print(f"Your estimated cost will be ${standcalcplancost}.")
            self.standcalcplannedhours = standcalcplanhours
            
    
            try:
                numstandcalc = int(numstandcalc)
            
            except ValueError:
                print("That is not a positive integer!")
                return -1
            
            if numstandcalc < 1:
                print("Invalid input. Number of standard calculators should be\
                    greater than zero!")
            else:
                self.standcalc =  numstandcalc
                return self.standcalc    
        
        
        if choice == 5:
            numscientcalc = input("How many scientific calculators would you\
                like to rent?")
            scientcalcplanhours = input("How many hours do you plan to rent for?")
            scientcalcplanhours = int(scientcalcplanhours)
            scientcalcplancost = (scientcalcplanhours)*7*numscientcalc
            print(f"Your estimated cost will be ${scientcalcplancost}.")
            self.scientcalcplannedhours = scientcalcplanhours
            
            
            try:
                numscientcalc = int(numscientcalc)
            
            except ValueError:
                print("That is not a positive integer!")
                return -1
            
            if numscientcalc < 1:
                print("Invalid input. Number of scientific calculators should\
                    be greater than zero!")
            else:
                self.scientcalc =  numscientcalc
                return self.scientcalc
            
        
        if choice == 6:
            numgraphcalc = input("How many graphing calculators would you like\
                to rent?")
            graphcalcplanhours = input("How many hours do you plan to rent for?")
            graphcalcplanhours = int(graphcalcplanhours)
            graphcalcplancost = (graphcalcplanhours)*10*numgraphcalc
            print(f"Your estimated cost will be ${graphcalcplancost}.")
            self.graphcalcplannedhours = graphcalcplanhours


            try:
                numgraphcalc = int(numgraphcalc)
            
            except ValueError:
                print("That is not a positive integer!")
                return -1
            
            if numgraphcalc < 1:
                print("Invalid input. Number of graphing calculators should\
                    be greater than zero!")
            else:
                self.graphcalc =  numgraphcalc
                return self.graphcalc
            
                              
    #JOSEPHINE'S 'CODE'         
    def returnItem(self, choice):
        """
        Allows customers to return their items to the rental shop.
        """
        
        if choice == 7:
            if self.goggrentalTime and self.goggles:
                return self.goggrentalTime, self.goggles, self.goggplannedhours
            
            else:
                return 0, 0, 0
            
            
        elif choice == 8:
            if self.labcoatrentalTime and self.labcoats:
                return self.labcoatrentalTime, self.labcoats,\
                    self.labcoatplannedhours
            
            else:
                return 0, 0, 0
            
            
        if choice == 9:
            if self.standcalcrentalTime and self.standcalc:
                return self.standcalcrentalTime, self.standcalc,\
                    self.standcalcplannedhours
            
            else:
                return 0, 0, 0 
        
        
        if choice == 10:
            if self.scientcalcrentalTime and self.scientcalc:
                return self.scientcalcrentalTime, self.scientcalc,\
                    self.scientcalcplannedhours
            
            else:
                return 0, 0, 0
            
            
        if choice == 11:
            if self.graphcalcrentalTime and self.graphcalc:
                return self.graphcalcrentalTime, self.graphcalc,\
                    self.graphcalcplannedhours
            
            else:
                return 0, 0, 0
        
        
        
        
        
        
        


def main():
    shop = LabRental(45, 30, 25, 40, 16)
    customer = Customer()

    while True:
        print("""
        =========== Lab Rental Shop ==============
        1. Display available stock 
        2. Request Goggles on hourly basis $9
        3. Request Lab Coats on hourly basis $25
        4. Request Standard Calculators on hourly basis $5
        5. Request Scientific Calculators on hourly basis $7
        6. Request Graphing Calculators on hourly basis $10
        7. Return Goggles
        8. Return Lab Coats
        9. Return Standard Calculators
        10. Return Scientific Calculators
        11. Return Graphing Calculators
        12. Exit
        """)
    
        choice = input("Enter choice: ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("That's not an int!")
            continue
        
        if choice == 1:
            shop.displaystock()
        
        elif choice == 2:
            customer.goggrentalTime = shop.rentItemOnHourlyBasis(choice, \
                customer.requestItem(choice))


        elif choice == 3:
            customer.labcoatrentalTime = shop.rentItemOnHourlyBasis(choice, \
                customer.requestItem(choice))


        elif choice == 4:
            customer.standcalcrentalTime = shop.rentItemOnHourlyBasis(choice, \
                customer.requestItem(choice))
            
            
        elif choice == 5:
            customer.scientcalcrentalTime = shop.rentItemOnHourlyBasis(choice, \
                customer.requestItem(choice))
            
        
        elif choice == 6:
            customer.graphcalcrentalTime = shop.rentItemOnHourlyBasis(choice, \
                customer.requestItem(choice))
            
               
        
        elif choice == 7:
            customer.bill = shop.returnItem(choice, customer.returnItem(choice))
            customer.goggrentalTime, customer.goggles = 0, 0
            customer.goggplannedhours = 0
            
            
        elif choice == 8:
            customer.bill = shop.returnItem(choice, customer.returnItem(choice))
            customer.labcoatrentalTime, customer.labcoats = 0, 0
            customer.labcoatplannedhours = 0
            
        
        elif choice == 9:
            customer.bill = shop.returnItem(choice, customer.returnItem(choice))
            customer.standcalcrentalTime, customer.standcalc = 0, 0
            customer.standcalcplannedhours = 0
            
            
        elif choice == 10:
            customer.bill = shop.returnItem(choice, customer.returnItem(choice))
            customer.scientcalcrentalTime, customer.scientcalc = 0, 0
            customer.scientcalcplannedhours = 0
            
            
        elif choice == 11:
            customer.bill = shop.returnItem(choice, customer.returnItem(choice))
            customer.graphcalcrentalTime, customer.graphcalc = 0, 0
            customer.graphcalcplannedhours = 0
        
                  
        elif choice == 12:
            break
        
        else:
            print("Invalid input. Please enter number between 1-12 ")        
    print("Thank you for using the lab rental system.")


if __name__=="__main__":
    main()