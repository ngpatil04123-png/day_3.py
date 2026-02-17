color=input("Enter  the light color :  ").lower()                #program to understand to light singnals in Aircraft navigation system
if color=="red":
    print("Red light: left side of aircraft or Stop signal")     #using some basic conditional statments like "if"
if color=="green":
    print("Green light: Right side of aircraft or Cleared to go")
if color=="white":
    print("White light: Aircraft tail or behind the aircraft")
if color=="yellow":
    print("Yellow light: Taxiway  guidance light")

#----------------------------------------------------------------------------------------------------------------------------

color=input("Enter  the light color :  ").lower()                #program to understand to light singnals in Aircraft navigation system
if color=="red":
    print("Red light: left side of aircraft or Stop signal")     #using some basic conditional statments like "if-elif-else"
elif color=="green":
    print("Green light: Right side of aircraft or Cleared to go")
elif color=="white":
    print("White light: Aircraft tail or behind the aircraft")
elif  color=="yellow":
    print("Yellow light: Taxiway  guidance light")
else:
    print(" invalied color entered: ")

#--------------------------------------------------------------------------------------------------------------------------

print("Aurcraft navigation System light singnal understanding")
print("1-  red light")                                            #program using number to print the aircraft singnals
print("2-  green light")
print("3-  white light")
print("4-  yellow light")
print("5-  invalied number")

num = int(input("Enter your choice  from(1-4) for color:"))

if num == 1:                                                      #using if-elif-else
    print("Red light : left side or Stop signal")
elif num==2:
    print("Green light : Right side or clear to go")
elif num == 3:
    print("white light: Aircraft tail or behind the aircraft")
elif num == 4:
    print("Yellow light: Taxiway guidance light")
else:
    print("invalid number")

#-----------------------------------------------------------------------------------------------------------------------------

print("Maritime navy light navigation system:")                   #maritime navy light navigation system
print("1-  red light : port side")
print("2-  green light : Starboard side")
print("3-  white light : visibality ")
print("4-  yellow light : special operations")
num=int(input("Enter your choice from(1-4): "))
if num == 1:
    print("Red light: you are seeing the left side of ship")      #using if-elif-else statment
elif num ==2:
    print("green light : you are seeing the left side of ship ")
elif num == 3:
    print("white light : if masthead light visible from front else visible from behind")
elif num ==4:
    print("yellow light : Towing vesseels or special operations like army operation")
else:
    print("invalid choice")

#------------------------------------------------------------------------------------------------------------------------------
print("sever status monitoring system :")                 #sever status monitoring system
print("1-  greenlight :")
print("2-  Amber/yellow light : ")
print("3-  red light :")
num=int(input("Enter your choice from(1-4): "))
if num == 1:
    print("Green light: Server operating normally ")      #using if-elif-else statment
elif num ==2:
    print("Amber/yellow:Warning!......check system")
    print("“Schedule maintenance”")
elif num == 3:
    print("Red light:!....system failure")
    print("--:Call technician immediatly:--")
else:
    print("invalid choice")

# #----------------------------------------------------------------------------------------------------------------------------

#lists in python
items=["rin","sugar","milk","pen"]
print(items[0])
items.pop(0)                  #deleting the eliments from list
print(items)
items.append("monaco")        #adding new element //mutable
items.remove("pen")           #removing element from list
items.insert(2,"laptop")      #adding in between two elements
items.index("milk")
items[0] = "book"       
items.clear()                 #clears the all elements  
print(items)
m=[[1,2],[3,4]]
print(m)

#-------------------------------------------------------------------------------------------------------------------------------------------

