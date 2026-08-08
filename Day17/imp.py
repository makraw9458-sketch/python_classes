import json


questions = [1,2,3,4,5,6,7,8,9]

# Save questions to file
with open('Day17/questions.json', 'w') as f:
    json.dump(questions, f, indent=2)

# Load questions from file
with open('questions.json', 'r') as f:
    questions = json.load(f)

# Save quiz results
# results = {"score": score, "total": len(questions), "date": timestamp}
# with open('results.json', 'w') as f:
#     json.dump(results, f)
