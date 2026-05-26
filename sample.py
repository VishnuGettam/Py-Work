class DateToday:

    # default constructor
    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def date_string_constructor(cls,date_str):
         day,month,year=map(int,date_str.split("-"))
         instance = cls(day,month,year)
         instance.final_date = str(day) + ":" + str(month) + ":" + str(year)
         return instance
    




if __name__ == "__main__":
    c1 = DateToday(3,5,2018)
    print( f" Date - {c1.day}/{c1.month}/{c1.year} ")

    c2 = DateToday.date_string_constructor("24-11-2012")    
    print( f" Date - {c2.day}/{c2.month}/{c2.year}  && { c2.final_date } ")

