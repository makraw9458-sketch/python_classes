questions = [
    {
        "question" : "What is the capital of France?",
        "options" : ["London","Paris","Berlin","Madrid",],
        "correct" : 1
    },
    # ds improvement
    {
        "question" : "What is 2 + 2?",
        "opt1" : "3",
        "opt2" : "4",
        "opt3" : "5",
        "opt4" : "6",
        "correct" : "B"
    },
    {
        "question" : "What is the color of the sky?",
        "opt1" : "Green",
        "opt2" : "Red",
        "opt3" : "Blue",
        "opt4" : "Yellow",
        "correct" : "C"
    },
    {
        "question" : "Which planet is known as the Red Planet?",
        "opt1" : "Venus",
        "opt2" : "Jupiter",
        "opt3" : "Mars",
        "opt4" : "Saturn",
        "correct" : "C"
    },
    {
        "question" : "What is the largest ocean on Earth?",
        "opt1" : "Atlantic",
        "opt2" : "Indian",
        "opt3" : "Arctic",
        "opt4" : "Pacific",
        "correct" : "D"
    }
]

userSelection = ""
score = 0

for question in questions:
    print(question['question'])
    print("\nOptions: \n")
    print("A. ",question.get('opt1', 'option not exist'))
    print("B. ",question.get('opt2', 'option not exist'))
    print("C. ",question.get('opt3', 'option not exist'))
    print("D. ",question.get('opt4', 'option not exist'))
    userSelection = input("Enter your option: ")
    print("\n\n")
    # logic to check correct opt.
    u_us = userSelection.upper()
    
    if u_us == question['correct']:
        score += 1

print("Your score is: ", score)



# FUNCTIONS
# ask question
# validate answer
# run quiz
# validate question shape (object structure)
# output [celebrate,]
# shuffle questions
# Add timer
# get data from file
# Save results to file
# Add difficulty levels
# add sections
# Allow retry on wrong answers
# review wrong answers
# users record and performance tracking