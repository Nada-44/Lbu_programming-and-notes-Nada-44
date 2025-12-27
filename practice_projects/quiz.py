want_play =  input("Do you want to play a quiz?: ").strip().lower()

if want_play != "yes":
    print("Maybe next time!")
    quit()
else:
    print("Great! Let's start the quiz.")
score = 0

answer1 = input("What is the capital of France? ").strip().lower()
if answer1 == "paris":
    print("Correct!")
    score += 1

answer2 = input("What is the capital of Germany? ").strip().lower()
if answer2 == "berlin":
    print("Correct!")
    score += 1

answer3 = input("What is the capital of England? ").strip().lower()
if answer3 == "London":
    print("Correct!")
    score += 1

answer4 = input("What is the capital of Egypt? ").strip().lower()
if answer4 == "Cairo":
    print("Correct!")
    score += 1

answer5 = input("What is the capital of Italy? ").strip().lower()
if answer5 == "rome":
    print("Correct!")
    score += 1

print(f"You got {score} out of 5 questions correct!")