# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 11:41:00 2022

@author: HP
"""

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
    if upper==1 and digit==1 and lower==1:
        print("Password accepted\n\n")
        return PW*3  #EncryptionOfPassword
    else:
        print("Password is invalid\n\n")
        PWord()
PWord()