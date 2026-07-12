questions = [
    [
        "What is the capital of France?",
        "A. London", 
        "B. Paris", 
        "C. Berlin", 
        "D. Madrid",
        "B"
    ],
    [
        "What is 2 + 2?",
        "A. 3", "B. 4", "C. 5", "D. 6"
        "B"
    ],
    [
        "What is the color of the sky?",
        "A. Green", "B. Red", "C. Blue", "D. Yellow"
        "C"
    ],
    [
        "Which planet is known as the Red Planet?",
        "A. Venus", "B. Jupiter", "C. Mars", "D. Saturn",
        "C"
    ],
    [
        "What is the largest ocean on Earth?",
        "A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific",
        "D"
    ]
]

userSelection = ""

for question in questions:
    print(question[0])
    print("\nOptions: \n")
    print(question[1])
    print(question[2])
    print(question[3])
    print(question[4])
    userSelection = input("Enter your option: ")
    print("\n\n")