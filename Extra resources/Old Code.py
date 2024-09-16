# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 17:28:22 2021
21
@author: HOME
"""

#Online Shopping Software

#Importing required modules
import datetime,mysql.connector,csv


def PWord():    #Shorya Panwar
    PW=input('''Create a strong password:
   -Password should be at least 8 characters long
   -Password should have at least 1 number, 1 uppercase
    character and 1 lowercase character.\n''')
    upper=lower=digit=0
    for dg in PW:
        if dg.isupper():
            upper=1
        if dg.isdigit():
            digit=1
        if dg.islower():
            lower=1 
    if upper==1 and digit==1 and lower==1 and len(PW)>=8:
        print("Password accepted\n\n")
        return PW*3  #EncryptionOfPassword
    else:
        print("Password is invalid\n\n")
        PWord()


def signin():   #Shorya Panwar
    global Name
    print("(1)Create Account")
    print("(2)Sign In")
    a=input("Enter your choice(1/2):\n")
    if a=='1':
        Name=input("Enter your full name:")
        Add=input("Enter your full address:")
        Phone=int(input("Enter your phone number:"))
        Email=input("Enter your Email address:")
        print('\n')
        PW=PWord()
        dbfile=open('UserDB.txt','a',newline='')
        writeobj=csv.writer(dbfile)
        writeobj.writerow([Name,Add,Phone,Email,PW])
        dbfile.close()
        main_menu()
        
    elif a=='2':
        dbfile=open('UserDB.txt','r',newline='')
        readerobj=csv.reader(dbfile)
        Name=input("Enter your full name:")
        P=(input("Enter your password:"))*3
        for record in readerobj:
            if len(record)>0:
                if record[0]==Name:
                    if record[4]==P:
                        print('Welcome back!\n\n')
                        main_menu()
                    
                    else:
                        print('Incorrect password\n\n')
                        signin()
            elif len(record)==0:
                print('Account does not exist\n\n')
                signin()
    else:
        print("Try again\n\n")
        signin()



def browse_items(): #Shorya Panwar
    global cart
    db=mysql.connector.connect(host='localhost',user='root',password='1234',database='Categories')
    cursor=db.cursor()
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
    choice=input('Enter your choice:')
    if choice=='1':
        choicerange=0
        print('S.No.\tItem\tPrice')
        for x in cursor.execute('SELECT * from Furniture;'):
            print(x[1],'\t',x[2],'\t',x[3])
            choicerange=choicerange+1
        itemchoice=int(input('Enter your preferred item:'))
        if itemchoice<=(choicerange):
            quantity=int(input('Enter quantity:'))
            l=list(x[2],x[3],quantity)
            cart.append(l)
            browse_items()
        else:
            print('Enter a valid choice number')
            browse_items()        
    
    elif choice=='2':
        itemlist=cursor.execute('SELECT * from Electronics;')
        print('S.No.\tItem\tPrice')
        for x in itemlist:
            print(x[1],'\t',x[2],'\t',x[3])
        itemchoice=int(input('Enter your preferred item:'))
        if itemchoice<=range(itemlist):
            quantity=int(input('Enter quantity:'))
            l=list(x[2],x[3],quantity)
            cart.append(l)
            browse_items()
        else:
            print('Enter a valid choice number')
            browse_items()     
    
    elif choice=='3':
        itemlist=cursor.execute('SELECT * from Kitchen;')
        print('S.No.\tItem\tPrice')
        for x in itemlist:
            print(x[1],'\t',x[2],'\t',x[3])
        itemchoice=int(input('Enter your preferred item:'))
        if itemchoice<=range(itemlist):
            quantity=int(input('Enter quantity:'))
            l=list(x[2],x[3],quantity)
            cart.append(l)
            browse_items()
        else:
            print('Enter a valid choice number')
            browse_items()     
    
    elif choice=='4':
        itemlist=cursor.execute('SELECT * from Fitness;')
        print('S.No.\tItem\tPrice')
        for x in itemlist:
            print(x[1],'\t',x[2],'\t',x[3])
        itemchoice=int(input('Enter your preferred item:'))
        if itemchoice<=range(itemlist):
            quantity=int(input('Enter quantity:'))
            l=list(x[2],x[3],quantity)
            cart.append(l)
            browse_items()
        else:
            print('Enter a valid choice number')
            browse_items()     
    
    elif choice=='5':
        itemlist=cursor.execute('SELECT * from Toys;')
        print('S.No.\tItem\tPrice')
        for x in itemlist:
            print(x[1],'\t',x[2],'\t',x[3])
        itemchoice=int(input('Enter your preferred item:'))
        if itemchoice<=range(itemlist):
            quantity=int(input('Enter quantity:'))
            l=list(x[2],x[3],quantity)
            cart.append(l)
            browse_items()
        else:
            print('Enter a valid choice number')
            browse_items()     
    
    elif choice=='6':
        itemlist=cursor.execute('SELECT * from Clothing;')
        print('S.No.\tItem\tPrice')
        for x in itemlist:
            print(x[1],'\t',x[2],'\t',x[3])
        itemchoice=int(input('Enter your preferred item:'))
        if itemchoice<=range(itemlist):
            quantity=int(input('Enter quantity:'))
            l=list(x[2],x[3],quantity)
            cart.append(l)
            browse_items()
        else:
            print('Enter a valid choice number')
            browse_items()     
    
    elif choice=='7':
        itemlist=cursor.execute('SELECT * from Hygiene_and_Beauty;')
        print('S.No.\tItem\tPrice')
        for x in itemlist:
            print(x[1],'\t',x[2],'\t',x[3])
        itemchoice=int(input('Enter your preferred item:'))
        if itemchoice<=range(itemlist):
            quantity=int(input('Enter quantity:'))
            l=list(x[2],x[3],quantity)
            cart.append(l)
            browse_items()
        else:
            print('Enter a valid choice number')
            browse_items()   
    
    elif choice=='8':
        itemlist=cursor.execute('SELECT * from Pantry;')
        print('S.No.\tItem\tPrice')
        for x in itemlist:
            print(x[1],'\t',x[2],'\t',x[3])
        itemchoice=int(input('Enter your preferred item:'))
        if itemchoice<=range(itemlist):
            quantity=int(input('Enter quantity:'))
            l=list(x[2],x[3],quantity)
            cart.append(l)
            browse_items()
        else:
            print('Enter a valid choice number')
            browse_items()     
    
    elif choice=='9':
        itemlist=cursor.execute('SELECT * from School_Supplies;')
        print('S.No.\tItem\tPrice')
        for x in itemlist:
            print(x[1],'\t',x[2],'\t',x[3])
        itemchoice=int(input('Enter your preferred item:'))
        if itemchoice<=range(itemlist):
            quantity=int(input('Enter quantity:'))
            l=list(x[2],x[3],quantity)
            cart.append(l)
            browse_items()
        else:
            print('Enter a valid choice number')
            browse_items()  
    
    elif choice=='10':
        itemlist=cursor.execute('SELECT * from Fashion_Accessories;')
        print('S.No.\tItem\tPrice')
        for x in itemlist:
            print(x[1],'\t',x[2],'\t',x[3])
        itemchoice=int(input('Enter your preferred item:'))
        if itemchoice<=range(itemlist):
            quantity=int(input('Enter quantity:'))
            l=list(x[2],x[3],quantity)
            cart.append(l)
            browse_items()
        else:
            print('Enter a valid choice number')
            browse_items()     
    else:
         print('Enter a valid choice number')
         browse_items()


def account():  #Shorya Panwar
    global Name
    dbfile=open('UserDB.txt','r',newline='')
    readerobj=csv.reader(dbfile)
    for record in readerobj:
        if len(record)==0:
            continue
        if record[0]==Name:
            print('Account Details\n')
            print('Name:',record[0])
            print('Address:',record[1])
            print('Phone:',record[2])
            print('Email:',record[3])
            print('\n\n')
            break
    main_menu()
        


def main_menu():    #Shorya Panwar
    while True:
        print('(1)Browse Items')
        print('(2)View Cart')
        print('(3)Proceed to Payment')
        print('(4)View Account Details')
        print('(5)Logout')
        choice=int(input('Enter your choice:'))
        if choice==1:
            browse_items()
        elif choice==2:
            view_cart()
        elif choice==3:
            payment()
        elif choice==4:
            account()
        elif choice==5:
            print('Thank you! Please shop again.\n\n')
            signin()
        else:
            print('Enter choice again\n\n')
            main_menu()
            
signin()
            
    
    
        
