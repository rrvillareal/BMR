# -*- coding: utf-8 -*-

def main():    
     metric = int(input("If used metric system press 1, if not press 2."))
     if metric == 1:
         
         print("Ex/ 1 Meter = 100 Centimeters!")
         height = float(input("What is your height in CENTIMETERS?: "))
         weight = float(input("What is your weight in KILOS?: "))
         age = int(input("What is your age?: "))
         gender = int(input("Type '1' if you're a boy and '2' if you're a girl: "))
         if gender == 1:
             Answer = MetricBoy(height, weight, age)
             print("Your BMR is: ", round(Answer, 1))
         else: 
             Answer = MetricGirl(height, weight, age)
             print("Your BMR is: ", round(Answer, 1))
     else:
        print("Ex/ 1 Foot = 12 Inches!" )
        height = float(input("What is your height in INCHES?: "))
        weight = float(input("What is your weight in POUNDS?: "))
        age = int(input("What is your age?: "))
        gender = int(input("Type '1' if you're a boy and '2' if you're a girl: "))
        if gender == 1:
            Answer = EnglishBoy(height, weight, age)
            print("Your BMR is: ", round(Answer, 1))
        else:
            Answer = EnglishGirl(height, weight, age)
            print("Your BMR is: ", round(Answer, 1))
          
def EnglishBoy(height, weight, age):
    newweight = (weight*(0.454))
    newheight = height*(2.54)
    MBMR = ((10*newweight)+(6.25*newheight)-(5*age)+5)
    return MBMR  

def EnglishGirl(height, weight, age):
    newweight = (weight*(0.453592))
    newheight = (height*(2.54))
    WBMR = ((10*newweight) + (6.25*newheight) - (5*age) -161)
    return WBMR
    
    
def MetricBoy(height, weight, age):
    MBMR = ((10*weight)+((6.25)*height)-(5*age)+5)
    return MBMR

def MetricGirl(height, weight, age):
    WBMR = ((10*weight)+((6.25)*height)-(5*age)-161)
    return WBMR
        
