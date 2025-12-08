import sys
import random
import os 




easy_puzzles = "easy_questions.txt"
medium_puzzles = "medium_questions.txt"
hard_puzzles = "hard_questions.txt"

def file_exists(filename):
    filepointer = os.path.exists(filename)


def load_puzzles(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read().strip()
    except FileNotFoundError:
        print(f"ERROR: Puzzle file '{filename}' not found!")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error reading {filename}: {e}")
        sys.exit(1)

    blocks = content.split("\n\n")
    puzzles = []

    for block in blocks:
        lines = block.strip().split("\n")
        if len(lines) < 3:
            continue
        question = lines[0].replace("question:", "").strip()
        hint = lines[1].replace("hint:", "").strip()
        answer = lines[2].replace("answer:", "").strip().lower()
        puzzles.append({"question": question, "hint": hint, "answer": answer})

    return puzzles


def get_user_choice(question, correct_answers):
    
    while True:
        user_input = input(question).strip().lower()
        if user_input in correct_answers:
            return user_input
        print("Invalid choice. Try again.\n")


def celebrate():
   messages = [
       "Doing great!!!!!!!",
       "Thinking smarttt",
       "well donee!!",
       "I am Impressedd :)",
       "Keep it upp!",
       "Nicee onee!",
   ]
   print(random.choice(messages), "\n")


def motivate(hint):
   messages = [
       "You can do it! come on",
       "Don't give up yet! ",
       "I believe in you!",
       "keep going, you're almost there!",
       "stay postive and try again!",
   ]
   print(random.choice(messages), "\n")
   print("Hint:", hint, "\n")


def ask_questions(puzzles):
    score = 0
    selected = random.sample(puzzles, 5)

    for number, quizz in enumerate(selected, start=1):
        print(f"Question {number}: {quizz['question']}")
        answer = input("Your answer: ").strip().lower()

        if answer == quizz["answer"]:
            celebrate()
            score += 2
        else:
            
            motivate(quizz["hint"])
            second_try = input("Try again: ").strip().lower()
            if second_try == quizz["answer"]:
                celebrate()
                score += 2
            else:
                print(f"The correct answer was: {quizz['answer']}\n")

    return score




def final_score(score):
   
   print(f"Your final score: {score} / 10")

   if score  >= 8:
     print("Impresive Work :)! You nailed it!")
   elif score >= 5:
     print("Good Job! You did well!")
   elif score >= 2:
     print("Not bad, but you can do better!")
   else:
    print("Don't give up! Try again and you'll improve!")


def choose_level():
    choice = input("Please choose a difficulty level:\n1. Easy\n2. Medium\n3. Hard\n").strip().lower()

    if choice in ["1", "easy"]:
        return easy_puzzles
    elif choice in ["2", "medium"]:
        return medium_puzzles
    elif choice in ["3", "hard"]:
        return hard_puzzles
    else:
        print("Invalid choice. Please select 1, 2, or 3 (or type Easy/Medium/Hard).")
        return choose_level()

   
    
def main():
    print("Welcome to MindMaze!")
    print("   -------------------------   ")
    print("Test your problem-solving skills with our exciting puzzles.\n")
    print("How the game works:")
    print("- You will get 5 questions, each worth 2 points.")
    print("- Correct answer = +2 points.")
    print("- If you answer wrong, don't worry you will have a 2nd chance, with a hint:).")
    print("- Maximum score: 10 points.\n")

    level_file = choose_level()

    print(f"\nLoading puzzles from '{level_file}'...\n")
    puzzles = load_puzzles(level_file)

    print("Great! Let's begin!\n")
    score = ask_questions(puzzles)

    final_score(score)


if __name__ == "__main__":
    main()




    