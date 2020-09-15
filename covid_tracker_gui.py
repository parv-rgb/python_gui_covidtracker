# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 01:44:42 2020

@author: parvp
"""


from covid import Covid
from tkinter import *


covidin= Covid()
root= Tk()
root.geometry("800x800")
root.title("Covid 19 Data")

"""def worldcases():
    print("total confirmed cases in world :", covidin.get_total_confirmed_cases())
    print("total active cases in world : ", covidin.get_total_active_cases())
    print("total recoverd :", covidin.get_total_recovered()) 
    print("total deaths :", covidin.get_total_deaths())"""
    


def info():
    try:
        root.update()
        if choice.get()=='world':
            Label(root, text="total confirmed cases in world :"+ str(covidin.get_total_confirmed_cases()), font="Consolas 13 ").pack(pady=30)
            Label(root, text="total active cases in world : " + str(covidin.get_total_active_cases()), font="Consolas 13").pack(pady=20)
            Label(root, text="total recoverd :" +str(covidin.get_total_recovered()), font="Consolas 13").pack(pady=20)
            Label(root, text="total deaths :" +str(covidin.get_total_deaths()), font="Consolas 13").pack(pady=20)
        else:
            root.update()
            cases=covidin.get_status_by_country_name(choice.get())
            for x,y in cases.items():
                Label(root, text= x +": "+ str(y), font="Consolas 13").pack(pady=10)
    except Exception as e:
        root.update()
        choice.set("Incorrect choice.... enter calmly")
    

                
        
            
    
    
    """if choice==1:
        worldcases()
    elif choice==2:
        print(" enter the country you are looking for:")
        con= input()
        cases= covidin.get_status_by_country_name(con)
        for x,y in cases.items():
            print(x, " : ", y)
    else:
        print("Dont be oversmart choose either 1 or 2")
        info()"""
        
Label(root, text="Get Updtaes On \n COVID-19", font="Consolas 25 bold").pack()

Label(root, text="For information on world cases : enter world", font="Consolas 15").pack(pady=10)
Label(root, text="For information of a country: enter country", font="Consolas 15 ").pack(pady=10)

myVar = StringVar()
myVar.set("Enter your choice below")
Entry(root, textvariable=myVar, width=40).pack(pady=20)

choice = StringVar()
Entry(root, textvariable=choice, width=40).pack(pady=20)

Button(root, text="Get Data", command=info).pack()


root.mainloop()

     

    