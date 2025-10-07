# Python Quiz Game

questions = (("How many elements are in the periodic table?: "),
           ("Name a character from final fantasy 10: "),
           ("What final fantasy is the character Cloud from?: "),
           ("How many pokemon are in Red / Blue version of the gameboy?: "),
           ("In Final Fantasy 15, what is the name of the main character?: "))

options = (("A. 116", "B. 117","C. 118", "D. 119"),
           ("A. Yuna", "B. Cloud","C. Zack", "D. Tifa"),
           ("A. 12", "B. 6","C. 3", "D. 7"),
           ("A. 251", "B. 351","C. 151", "D. 751"),
           ("A. Areith", "B. Tidus","C. Zack", "D. Noctis"))


answers = ("C", "A", "D", "C", "D")

guesses = []

score = 0
question_num = 0

for question in questions:
    print("-----------------------")
    print(question)
    for option in options[question_num]:
        print(option)
        print()
        
    guess = input("Enter (A, B, C, D):").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT! ! !")
    else:
        print("INCORRECT! :( ")
        print(f"{answers[question_num]} is the correct answer. ")
        print()
        
            
    question_num += 1
    
print("------------------------")
print("       RESULTS          ")
print("------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()
print("guesses: ", end="")
for guess in guesses:
    print(guess, end= " ")
print()

score = int(score / len(questions) * 100)
print(f"Your Score is: {score}%")
    