# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 12:15:01 2022

@author: HP
"""

#Importing required modules
import csv

cart=[]
info=[]



def signin():   
    global info
    print('___________________')
   
    print('\nSIGN IN SCREEN\n')
    print('___________________')
    print("Please give your details:")
    Name=input("Enter your full name:")
    Add=input("Enter your full address:")
    Phone=int(input("Enter your phone number:"))
    Email=input("Enter your Email address:")
    print('\n')
    info=[Name,Add,Phone,Email]
    main_menu()



def browse_items(): 
    global cart
    print('Select your desired category:\n\n')
    print('(1)Furniture')
    print('(2)Electronics')
    print('(3)Kitchen')
    print('(4)Fitness')
    print('(5)Toys')
    print('(6)Clothing')
    print('(7)Hygiene & Beauty')
    print('(8)Pantry')
    print('(9)School Supplies')
    print('(10)Fashion Accessories')
    print('(11)Back to main menu')
    choice=input('Enter your choice:')
    print('\n\n')
    if choice=='1':
        allitems=[]
        chrange=0
        fh=open('Furniture.txt','r')
        readerobj=csv.reader(fh)
        print('No.Item\t\t\t Price')
        for record in readerobj:
            allitems.append(record)
            print(record[0],record[1],'\t',record[2])
            chrange+=1
        choice=int(input('Enter a choice as a number:'))
        if choice<=chrange:
            quantity=int(input('Enter quantity:'))
            cart.append([allitems[choice-1][1],allitems[choice-1][2],quantity])
            print('Item shopped successfully!')
            browse_items()
        else:
            print('Invalid choice')
            browse_items()
            
    elif choice=='2':
        allitems=[]
        chrange=0
        fh=open('Electronics.txt','r')
        readerobj=csv.reader(fh)
        print('No.Item\t\t\t Price')
        for record in readerobj:
            allitems.append(record)
            print(record[0],record[1],'\t',record[2])
            chrange+=1
        choice=int(input('Enter a choice as a number:'))
        if choice<=chrange:
            quantity=int(input('Enter quantity:'))
            cart.append([allitems[choice-1][1],allitems[choice-1][2],quantity])
            print('Item shopped successfully!')
            browse_items()
        else:
            print('Invalid choice')
            browse_items()
            
    elif choice=='3':
        allitems=[]
        chrange=0
        fh=open('Kitchen.txt','r')
        readerobj=csv.reader(fh)
        print('No.Item\t\t\t Price')
        for record in readerobj:
            allitems.append(record)
            print(record[0],record[1],'\t',record[2])
            chrange+=1
        choice=int(input('Enter a choice as a number:'))
        if choice<=chrange:
            quantity=int(input('Enter quantity:'))
            cart.append([allitems[choice-1][1],allitems[choice-1][2],quantity])
            print('Item shopped successfully!')
            browse_items()
        else:
            print('Invalid choice')
            browse_items()
            
    elif choice=='4':
        allitems=[]
        chrange=0
        fh=open('Fitness.txt','r')
        readerobj=csv.reader(fh)
        print('No.Item\t\t\t Price')
        for record in readerobj:
            allitems.append(record)
            print(record[0],record[1],'\t',record[2])
            chrange+=1
        choice=int(input('Enter a choice as a number:'))
        if choice<=chrange:
            quantity=int(input('Enter quantity:'))
            cart.append([allitems[choice-1][1],allitems[choice-1][2],quantity])
            print('Item shopped successfully!')
            browse_items()
        else:
            print('Invalid choice')
            browse_items()
            
    elif choice=='5':
        allitems=[]
        chrange=0
        fh=open('Toys.txt','r')
        readerobj=csv.reader(fh)
        print('No.Item\t\t\t Price')
        for record in readerobj:
            allitems.append(record)
            print(record[0],record[1],'\t',record[2])
            chrange+=1
        choice=int(input('Enter a choice as a number:'))
        if choice<=chrange:
            quantity=int(input('Enter quantity:'))
            cart.append([allitems[choice-1][1],allitems[choice-1][2],quantity])
            print('Item shopped successfully!')
            browse_items()
        else:
            print('Invalid choice')
            browse_items()
            
    elif choice=='6':
        allitems=[]
        chrange=0
        fh=open('Clothing.txt','r')
        readerobj=csv.reader(fh)
        print('No.Item\t\t\t Price')
        for record in readerobj:
            allitems.append(record)
            print(record[0],record[1],'\t',record[2])
            chrange+=1
        choice=int(input('Enter a choice as a number:'))
        if choice<=chrange:
            quantity=int(input('Enter quantity:'))
            cart.append([allitems[choice-1][1],allitems[choice-1][2],quantity])
            print('Item shopped successfully!')
            browse_items()
        else:
            print('Invalid choice')
            browse_items()
            
    elif choice=='7':
        allitems=[]
        chrange=0
        fh=open('Hygiene&Beauty.txt','r')
        readerobj=csv.reader(fh)
        print('No.Item\t\t\t Price')
        for record in readerobj:
            allitems.append(record)
            print(record[0],record[1],'\t',record[2])
            chrange+=1
        choice=int(input('Enter a choice as a number:'))
        if choice<=chrange:
            quantity=int(input('Enter quantity:'))
            cart.append([allitems[choice-1][1],allitems[choice-1][2],quantity])
            print('Item shopped successfully!')
            browse_items()
        else:
            print('Invalid choice')
            browse_items()
            
    elif choice=='8':
        allitems=[]
        chrange=0
        fh=open('Pantry.txt','r')
        readerobj=csv.reader(fh)
        print('No.Item\t\t\t Price')
        for record in readerobj:
            allitems.append(record)
            print(record[0],record[1],'\t',record[2])
            chrange+=1
        choice=int(input('Enter a choice as a number:'))
        if choice<=chrange:
            quantity=int(input('Enter quantity:'))
            cart.append([allitems[choice-1][1],allitems[choice-1][2],quantity])
            print('Item shopped successfully!')
            browse_items()
        else:
            print('Invalid choice')
            browse_items()
            
    elif choice=='9':
        allitems=[]
        chrange=0
        fh=open('School Supplies.txt','r')
        readerobj=csv.reader(fh)
        print('No.Item\t\t\t Price')
        for record in readerobj:
            allitems.append(record)
            print(record[0],record[1],'\t',record[2])
            chrange+=1
        choice=int(input('Enter a choice as a number:'))
        if choice<=chrange:
            quantity=int(input('Enter quantity:'))
            cart.append([allitems[choice-1][1],allitems[choice-1][2],quantity])
            print('Item shopped successfully!')
            browse_items()
        else:
            print('Invalid choice')
            browse_items()
            
    elif choice=='10':
        allitems=[]
        chrange=0
        fh=open('Fashion Accessories.txt','r')
        readerobj=csv.reader(fh)
        print('No.Item\t\t\t Price')
        for record in readerobj:
            allitems.append(record)
            print(record[0],record[1],'\t',record[2])
            chrange+=1
        choice=int(input('Enter a choice as a number:'))
        if choice<=chrange:
            quantity=int(input('Enter quantity:'))
            cart.append([allitems[choice-1][1],allitems[choice-1][2],quantity])
            print('Item shopped successfully!')
            browse_items()
        else:
            print('Invalid choice')
            browse_items()
           
    elif choice=='11':
        main_menu()
        
    else:
        print('Invalid choice\n\n')
        browse_items()
        
        
def view_cart():    
    if len(cart)>0:
        print('\nItem\t\tPrice\tQuantity\t')
        for itemlist in cart:
            print(itemlist[0],itemlist[1],'\t',itemlist[2])
    else:
        print('\n\nEmpty cart\n\n')
        
        
def clear_cart():   
    global cart
    choice=input('\n\nAre you sure you want to clear your cart?(y/n):')
    if choice=='y':
        cart=[]
    elif choice=='n':
        main_menu()
    else:
        print('Enter a vaild choice\n\n')
        main_menu()
        
        
def payment():
    if len(cart)>0:
        print('Your billing details are:\n')
        account()
        print('\nThe items you bought are:\n')
        view_cart()
        print('Your total will be:',end='')
        total=0
        for item in cart:
            total+=eval(item[1])*item[2]
        print(total)
        choice=input('\n\nWould you like to continue(y/n):')
        if choice=='y':
            print('\n\nThanks for shopping! Please return soon!\n\n')
            signin()
        elif choice=='n':
            main_menu()
        else:
            print('\n\nPlease enter a valid choice\n\n')
            payment()
    else:
        print('\nEmpty cart\n')
        main_menu()
        

def account():  
    global info
    print('\n\nAccount Details\n')
    print('Name:',info[0])
    print('Address:',info[1])
    print('Phone:',info[2])
    print('Email:',info[3])
    print('\n\n')



def modify_account():
    change=input('\n\nWould you like to change the given information?(y/n)')
    if change=='y':
        signin()
    else:
        main_menu()



def main_menu(): 
    global cart
    while True:
        print('\n\n')
        print('(1)Browse Items')
        print('(2)View Cart')
        print('(3)Clear cart')
        print('(4)Proceed to Payment')
        print('(5)View Account Details')
        print('(6)Modify Account')
        print('(7)Logout')
        choice=input('\nEnter your choice:')
        if choice=='1':
            browse_items()
        elif choice=='2':
            view_cart()
        elif choice=='3':
            clear_cart()
        elif choice=='4':
            payment()
        elif choice=='5':
            account()
        elif choice=='6':
            modify_account()
        elif choice=='7':
            print('Thank you! Please shop again.\n\n')
            cart=[]
            signin()
        else:
            print('\nEnter choice again:')
            main_menu()

signin()




#     CREDITS   
#  Vatsal Verma  12 A+   
#  Vijit Verma   12 A+   
 
#  S D Public School
#UNDER THE GUIDANCE OF:
#  Mr. Sapan Jain
