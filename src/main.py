#------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    Question_num = 1
    
    for key in question:
        print("--------------------")
        print(key)
        for i in options[Question_num-1]:
           print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)
        
        correct_guesses += check_answer(question.get(key), guess)
        
        Question_num += 1
        
    display_score(correct_guesses, guess)
    
#-------------------------
def check_answer(answer, guess):
    if answer == guess:
         print("CORRECT!")
         return 1
    else:
        print("WRONG!")
        return 0
         
    
#------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("--------------------------")
    
    print("Answers: ", end="")
    for i in question:
        print(question.get(i), end=" ")
    print()
    
    
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
    
    score = int((correct_guesses/len(question))*100)
    print("Your score is: "+str(score)+"%")
    
#-------------------------
def play_again():
    response = input("Do you want to again? (yes or no): ").upper()
    if response == "YES":
       return True
    else:
       return False
    
    
#--------------------------

question = {
   "who created python?: ": "A",
   "What year was python created?: ": "B",
   "python is tributed to which comedy group?: ": "C",
   "Is the Earth round? ": "A"
}

options = [["A. Guido van rossum","B. Elon musk","C. Bill gate","D. Mark Zuckerburg"],
          ["A.1989", "B.1991","C.2000","D.2016"],
          ["A. lonely Island","B. smosh","C. monty python", "D. SNL"],
          ["A. True","B. False","C. sometimes","D. what's Earth"]]
      

new_game()  
while play_again():
     new_game()
     
print("Byeeeeee!")
  
          
          
          
          
          
          
          
          