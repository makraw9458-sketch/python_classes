Here are examples of basic and useful external functions you can import:

## **1. Random Module - For Selection & Shuffling**
```python
import random

# Shuffle quiz questions
questions = [...]
random.shuffle(questions)

# Pick random question
q = random.choice(questions)

# Generate random number for difficulty
difficulty = random.randint(1, 5)
```

## **2. Time Module - For Timers & Delays**
```python
import time

# Timer
start = time.time()
# ... run quiz ...
elapsed = time.time() - start
print(f"Time taken: {elapsed:.2f} seconds")

# Add delays for better UX
print("Starting quiz...")
time.sleep(1)  # Pause 1 second

# Date/time stamp for results
from datetime import datetime
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

## **3. OS Module - File & System Operations**
```python
import os

# Check if file exists
if os.path.exists("quiz_results.txt"):
    print("Previous results found!")

# Create folder for results
os.makedirs("results", exist_ok=True)

# Clear screen (platform specific)
os.system('cls' if os.name == 'nt' else 'clear')
```

## **4. JSON Module - Save/Load Data**
```python
import json

# Save questions to file
with open('questions.json', 'w') as f:
    json.dump(questions, f, indent=2)

# Load questions from file
with open('questions.json', 'r') as f:
    questions = json.load(f)

# Save quiz results
results = {"score": score, "total": len(questions), "date": timestamp}
with open('results.json', 'w') as f:
    json.dump(results, f)
```

## **5. Sys Module - Command Line Arguments**
```python
import sys

# Get command line arguments
if len(sys.argv) > 1:
    difficulty = sys.argv[1]  # python quiz.py easy
else:
    difficulty = "medium"

# Exit program
if not questions:
    print("No questions available!")
    sys.exit(1)
```

## **6. Math Module - Basic Math Functions**
```python
import math

# Round up percentage
percentage = (score / total) * 100
rounded = math.ceil(percentage)  # Round up

# Or round down
rounded = math.floor(percentage)
```

## **7. Re Module - Pattern Matching**
```python
import re

# Validate email for user registration
email = input("Enter email: ")
if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
    print("Valid email")

# Extract numbers from text
text = "Score: 85 out of 100"
numbers = re.findall(r'\d+', text)  # ['85', '100']
```

## **8. Collections - Advanced Data Structures**
```python
from collections import Counter, defaultdict

# Count wrong answers
wrong_answers = ['A', 'B', 'A', 'C', 'B']
count = Counter(wrong_answers)
print(count)  # Counter({'A': 2, 'B': 2, 'C': 1})

# Default dictionary for categories
from collections import defaultdict
questions_by_difficulty = defaultdict(list)
for q in questions:
    questions_by_difficulty[q['difficulty']].append(q)
```

## **9. Complete Quiz Example with Imports**
```python
import json
import random
import time
import os
from datetime import datetime
from collections import Counter

def load_questions():
    """Load questions from JSON file"""
    try:
        with open('questions.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Questions file not found!")
        return []

def save_results(score, total, wrong_answers):
    """Save results to file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    results = {
        "date": timestamp,
        "score": score,
        "total": total,
        "percentage": (score/total)*100,
        "wrong": wrong_answers
    }
    
    # Save as JSON
    with open('results.json', 'a') as f:
        json.dump(results, f)
        f.write('\n')
    
    # Also save readable text
    with open('results.txt', 'a') as f:
        f.write(f"{timestamp} - Score: {score}/{total}\n")

def main():
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Load questions
    questions = load_questions()
    if not questions:
        print("No questions available!")
        return
    
    # Shuffle
    random.shuffle(questions)
    
    # Start timer
    start = time.time()
    score = 0
    wrong = []
    
    for idx, q in enumerate(questions, 1):
        print(f"\n📝 Q{idx}/{len(questions)}")
        print(q['question'])
        
        # Show options
        for i, opt in enumerate(q['options']):
            print(f"{chr(65+i)}. {opt}")
        
        # Get answer
        answer = input("Your answer: ").upper()
        
        # Check
        if answer == q['correct']:
            score += 1
            print("✅ Correct!")
        else:
            wrong.append(q['question'])
            print(f"❌ Wrong! Correct: {q['correct']}")
        
        time.sleep(0.5)  # Small pause
    
    # Calculate results
    elapsed = time.time() - start
    
    # Show summary
    print(f"\n{'='*50}")
    print(f"Score: {score}/{len(questions)}")
    print(f"Percentage: {(score/len(questions))*100:.1f}%")
    print(f"Time: {elapsed:.1f} seconds")
    
    if wrong:
        print(f"\nYou got {len(wrong)} questions wrong.")
        for q in wrong:
            print(f"  - {q}")
    
    # Save results
    save_results(score, len(questions), wrong)

if __name__ == "__main__":
    main()
```

## **10. Bonus Useful Imports**

```python
# For ASCII art or formatting
import pyfiglet  # pip install pyfiglet
text = pyfiglet.figlet_format("QUIZ")
print(text)

# For colored output
from colorama import Fore, Style  # pip install colorama
print(Fore.GREEN + "Correct!" + Style.RESET_ALL)
print(Fore.RED + "Wrong!" + Style.RESET_ALL)

# For progress bars
from tqdm import tqdm  # pip install tqdm
for i in tqdm(range(10)):
    time.sleep(0.1)
```

## **Most Essential for Your Quiz App:**
1. **`random`** - Shuffle questions, randomize options
2. **`json`** - Save/load question banks
3. **`time`** - Timer, delays
4. **`os`** - File operations, clear screen
5. **`datetime`** - Timestamp results
6. **`collections`** - Counter for statistics

These imports will make your quiz app much more professional and functional!