import os
import random
import time

while 1 == 1:

    os.system("cls")

    input("Press Enter To Roll")
    
    os.system("cls")
    print("Rolling.")
    time.sleep(.5)
    
    os.system("cls")
    print("Rolling..")
    time.sleep(.5)
    
    os.system("cls")
    print("Rolling...")
    time.sleep(.5)
    
    
    os.system("cls")
    print("Rolling.")
    time.sleep(.5)
    
    os.system("cls")
    print("Rolling..")
    time.sleep(.5)
    
    os.system("cls")
    print("Rolling...")
    time.sleep(.5)
    
    
    os.system("cls")
    print("Rolling.")
    time.sleep(.5)
    
    os.system("cls")
    print("Rolling..")
    time.sleep(.5)
    
    os.system("cls")
    print("Rolling...")
    time.sleep(.5)
    
    print("")
    
    number = random.randint(1,6)
    
    if number == 1:
        print('''
        -----
        |   |
        | o |
        |   |
        -----
        ''')
    if number == 2:
        print('''
        -----
        |o  |
        |   |
        |  o|
        -----
        ''')
        
    if number == 3:
        print('''
        -----
        |o  |
        | o |
        |  o|
        -----
        ''')
        
    if number == 4:
        print('''
       -----
       |o o|
       |   |
       |o o|
       -----
        ''')
        
    if number == 5:
        print('''
      -----
      |o o|
      | o |
      |o o|
      -----
        ''')
        
    if number == 6:
        print('''
       -----
       |o o|
       |o o|
       |o o|
       -----
        ''')
  

    print("You got a " + str(number) + "!")
    
    input("")