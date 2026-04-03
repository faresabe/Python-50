import random

# the .randrange() function generates a
# random number within the specified range.
num = random.randrange(1000, 10000)
num_str = str(num)  # Convert once

n = int(input("Guess the 4 digit number:"))

# condition to test equality of the
# guess made. Program terminates if true.
if (n == num):
    print("Great! You guessed the number in just 1 try! You're a Mastermind!")
else:
    # ctr variable initialized. It will keep count of
    # the number of tries the Player takes to guess the number.
    ctr = 0

    # while loop repeats as long as the
    # Player fails to guess the number correctly.
    while (n != num):
        # variable increments every time the loop
        # is executed, giving an idea of how many
        # guesses were made.
        ctr += 1

        # explicit type conversion of an integer to
        # a string in order to ease extraction of digits
        n_str = str(n)

        bulls = 0
        cows = 0
        used = [False] * 4

        # First, count bulls (correct position)
        for i in range(4):
            if n_str[i] == num_str[i]:
                bulls += 1
                used[i] = True

        # Then, count cows (correct digit, wrong position)
        for i in range(4):
            if not used[i]:  # Only check if not already a bull
                for j in range(4):
                    if not used[j] and n_str[i] == num_str[j]:
                        cows += 1
                        used[j] = True
                        break

        if bulls == 4:
            break  # Should not happen here, but safety

        print(f"Not quite the number. Bulls: {bulls}, Cows: {cows}")
        n = int(input("Enter your next choice of numbers: "))

    # After loop, success
    print("You've become a Mastermind!")
    print("It took you only", ctr + 1, "tries.")