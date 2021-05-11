#!/usr/bin/env python3
#Title: Calculator
#Author: My7H

import time

y = "\033[2;33m"
g = "\033[2;32m"
w = "\033[2;37m"
r = "\033[2;31m"
u = "\033[4m"

def addition(num1, num2):
    ans = num1 + num2
    print(g+"\n["+w+"•"+g+"] "+y+"Ans ="+w+"", ans)
    
def subtract(num1, num2):
    ans = num1 - num2
    print(g+"\n["+w+"•"+g+"] "+y+"Ans ="+w+"", ans)
    
def divide(num1, num2):
    ans = num1 / num2
    print(g+"\n["+w+"•"+g+"] "+y+"Ans ="+w+"", ans)
    
def mul(num1, num2):
    ans = num1 * num2
    print(g+"\n["+w+"•"+g+"] "+y+"Ans ="+w+"", ans)
    
def rtp(num1, num2):
    ans = num1 ** num2
    print(g+"\n["+w+"•"+g+"] "+y+"Ans ="+w+"", ans)
   
print(g+"            >>"+w+"×"+y+" SIMPLE CALCULATOR!"+w+" ×"+g+"<<")
time.sleep(0.5)
print()
print(g+"["+w+"*"+g+"]"+y+" Hi, what's your name?")
time.sleep(0.5)
name = input(g+">>"+y+" ")
print()
time.sleep(0.5)
print(g+"["+w+"✓"+g+"]"+y+" Welcome "+name+", Lets Calculate!")
time.sleep(0.5)
print(g+"\n["+w+"*"+g+"]"+y+" SYMBOLS ("+w+"$"+y+") : \nAdd ("+w+"+"+y+"), Subtract ("+w+"-"+y+"), Divide ("+w+"/"+y+"), Multiply ("+w+"* "+g+"or "+w+"x"+y+"),\nRaise to power ("+w+"^"+y+")")

while True:
    try :
        num1 = int(input("\n"+g+"➢ "+y+"Num:"+w+" "))
        sign = input(g+"➢  "+y+"$ : "+w+"")
        num2 = int(input(g+"➢ "+y+"Num:"+w+" "))
        
        if sign == "+" :
            time.sleep(0.5)    
            addition(num1, num2)
            print(y+"\nTo re-calculate Press [Enter] else, press '"+g+"N"+y+"' to exit")
            reply = input(g+"\n>> "+y+"")
            if reply == "n" or reply == "N" :
                print(g+"\n["+w+"✓"+g+"]"+y+" Bye "+name+"!")
                break
            else:
                continue

        elif sign == "-" :
            subtract(num1, num2)
            print(y+"\nTo re-calculate Press [Enter] else, press '"+g+"N"+y+"' to exit")
            reply = input(g+"\n>> "+y+"")
            if reply == "n" or reply == "N" :
                print(g+"\n["+w+"✓"+g+"]"+y+" Bye "+name+"!")
                break
            else:
                continue

        elif sign == "/" :
            divide(num1, num2)
            print(y+"\nTo re-calculate Press [Enter] else, press '"+g+"N"+y+"' to exit")
            reply = input(g+"\n>> "+y+"")
            if reply == "n" or reply == "N" :
                print(g+"\n["+w+"✓"+g+"]"+y+" Bye "+name+"!")
                break
            else:
                continue

        elif sign == "*" or sign == "x" or sign == "×" :
            mul(num1, num2)
            print(y+"\nTo re-calculate Press [Enter] else, press '"+g+"N"+y+"' to exit")
            reply = input(g+"\n>> "+y+"")
            if reply == "n" or reply == "N" :
                print(g+"\n["+w+"✓"+g+"]"+y+" Bye "+name+"!")
                break
            else:
                continue

        elif sign == "^" :
            rtp(num1, num2)
            print(y+"\nTo re-calculate Press [Enter] else, press '"+g+"N"+y+"' to exit")
            reply = input(g+"\n>> "+y+"")
            if reply == "n" or reply == "N" :
                print(g+"\n["+w+"✓"+g+"]"+y+" Bye "+name+"!")
                break
            else:
                continue

        else:
            print(g+"\n["+w+"×"+g+"] "+r+"Unknown Input")
            
    except :
        print(g+"\n["+w+"×"+g+"] "+r+"Invalid! "+y+"That was no number")
            


