import random

num = random.randint(1, 10)
guess = ""
count = 0
max = 3
out = False

   
while guess != num and not out: 
    if count < max:
       try:
          guess= int(input("Enter your guess(1-10): "))
          count += 1

          if guess < num:
            print("The number is bigger" )

          elif guess > num:
             print("The number is smaller")
       except ValueError:
        print("Please enter a valid number between 1 and 10.")
     
  
    else:
      out = True


if out:
    print("You lost! The number was", num)

else:
    print("correct! You Won!")
