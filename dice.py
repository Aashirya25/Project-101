import random 
import time
print ("Welcome to Roll a dice!")
time.sleep(1)
ask = input("Would you like to roll the dice?")

while (ask != "no" or "nah" or "nope"):
    time.sleep(1)
    print ("The dice will roll in 3 seconds")
    time.sleep(1)
    i=3
    while i > 0:
        min = int(i/60)
        sec = int(i%60)
        timer = f'{min}:{sec}'
        print(timer,end="\r")
        time.sleep(1)
        i-=1

    no = random.randint(1,6) 
      
    if no == 1: 
        print("[-----]") 
        print("[     ]") 
        print("[  0  ]") 
        print("[     ]") 
        print("[-----]") 
    if no == 2: 
        print("[-----]") 
        print("[ 0   ]") 
        print("[     ]") 
        print("[   0 ]") 
        print("[-----]") 
    if no == 3: 
        print("[-----]") 
        print("[     ]") 
        print("[0 0 0]") 
        print("[     ]") 
        print("[-----]") 
    if no == 4: 
        print("[-----]") 
        print("[0   0]") 
        print("[     ]") 
        print("[0   0]") 
        print("[-----]") 
    if no == 5: 
        print("[-----]") 
        print("[0   0]") 
        print("[  0  ]") 
        print("[0   0]") 
        print("[-----]") 
    if no == 6: 
        print("[-----]") 
        print("[0 0 0]") 
        print("[     ]") 
        print("[0 0 0]") 
        print("[-----]") 


    response=input("Would you like to roll again?:") 
    print("\n") 

    while response != "no": 
        time.sleep(2) 
        no = random.randint(1,6) 
      
        if no == 1: 
            print("[-----]") 
            print("[     ]") 
            print("[  0  ]") 
            print("[     ]") 
            print("[-----]") 
        if no == 2: 
            print("[-----]") 
            print("[ 0   ]") 
            print("[     ]") 
            print("[   0 ]") 
            print("[-----]") 
        if no == 3: 
            print("[-----]") 
            print("[     ]") 
            print("[0 0 0]") 
            print("[     ]") 
            print("[-----]") 
        if no == 4: 
            print("[-----]") 
            print("[0   0]") 
            print("[     ]") 
            print("[0   0]") 
            print("[-----]") 
        if no == 5: 
            print("[-----]") 
            print("[0   0]") 
            print("[  0  ]") 
            print("[0   0]") 
            print("[-----]") 
        if no == 6: 
            print("[-----]") 
            print("[0 0 0]") 
            print("[     ]") 
            print("[0 0 0]") 
            print("[-----]") 
            
        response=input("Would you like to roll again?:") 
        print("\n") 

    else:
        print("Thank you for rolling a dice with us! Goodbye!")
        break
    
