import random
import math
UpperBound = int(input("Enter the Upper Bound Number: "))
LowerBound = int(input("Enter the Lower Bound Number: "))


if LowerBound > UpperBound:
    print("Lower bound must be less than upper bound")
    exit()

Num = random.randint(LowerBound,UpperBound)
Loop = int(math.ceil(math.log(UpperBound - LowerBound + 1 ,2)))
Won = False

while Loop > 0:
    
    try:
         Ask = int(input("Guess A Number: "))
    except ValueError:
        print("Enter a valid number")
    


   
    if Ask > Num:
        print("Number too High Try Again")
    elif Ask < Num:
        print("Number too Low Try Again")
    else:
        Won = True
        print("Congra , YOU WON")
        break
    Loop -=1  

if Won == False:
  print("You Lose the number was," , Num)  
