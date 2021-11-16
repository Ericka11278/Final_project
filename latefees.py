from datetime import datetime


def lateFees(self, user_request): 
    """
    - This method will go through the  items rented out, the date they were rented, the days they were planned/requested to be rented out for by an
    individual, and will compute a late fee based on the items  request and how late 
    """
    rentLabCoat, rentCalculator, rentGoggles,rentDate, plannedRentDays = user_request
    
    if rentDate and rentLabCoat or rentCalculator or rentGoggles: 
        self.return_date = datetime.now()
        rentalPeriod = self.return_date - rentDate
        if rentalPeriod > plannedRentDays: 
            days_late = round(rentalPeriod) - plannedRentDays
            if rentLabCoat: 
                coat_late_fee = days_late * 7
            else: 
                coat_late_fee = 0 
            if rentCalculator: 
                cal_late_fee = days_late * 10
            else: 
                cal_late_fee = 0 
            if rentGoggles: 
                goggle_late_fee = days_late * 5
            else: 
                goggle_late_fee = 0
    return (coat_late_fee + cal_late_fee + goggle_late_fee) 