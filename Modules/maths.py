
"""
    importing the module 
        built -in (math,datetime) https://docs.python.org/3/py-modindex.html
        published (flask,django) https://pypi.org/
"""
import math as m
import datetime as dt

def Area_Circle(radius:int):
    return m.pi * radius * radius



if __name__ == "__main__":
    rad = int(input("Enter the radius : "))

    todays_date = dt.date.today()


    print(Area_Circle(radius=rad))
    print(f"Todays Date : {todays_date}")