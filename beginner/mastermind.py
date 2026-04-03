import random


num = random.randrange(1000, 10000)
num_str = str(num)  

n = int(input("Guess the 4 digit number:"))


if (n == num):
    print("Great! You guessed the number in just 1 try! You're a Mastermind!")
else:
    
    ctr = 0

    
    while (n != num):
       
        ctr += 1

        
        n_str = str(n)

        bulls = 0
        cows = 0
        used = [False] * 4

        
        for i in range(4):
            if n_str[i] == num_str[i]:
                bulls += 1
                used[i] = True

        
        for i in range(4):
            if not used[i]: 
                for j in range(4):
                    if not used[j] and n_str[i] == num_str[j]:
                        cows += 1
                        used[j] = True
                        break

        if bulls == 4:
            break 

        print(f"Not quite the number. Bulls: {bulls}, Cows: {cows}")
        n = int(input("Enter your next choice of numbers: "))

   
    print("You've become a Mastermind!")
    print("It took you only", ctr + 1, "tries.")