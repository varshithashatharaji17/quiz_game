# Quiz Questions
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Delhi", "B. Mumbai", "C. Kolkata", "D. Chennai"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer": "C"
    },
    {
        "question": "Who developed Python programming language?",
        "options": ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
        "answer": "A"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"],
        "answer": "D"
    },
    {
        "question": "Which data structure uses FIFO order?",
        "options": ["A. Stack", "B. Queue", "C. Tree", "D. Graph"],
        "answer": "B"
    }
]

# Initialize score
score = 0

# Start Quiz
print("Welcome to the Quiz Game! 🧠")
print("-" * 40)

# Loop through questions
for idx, q in enumerate(questions, start=1):
    print(f"\nQuestion {idx}: {q['question']}")
    for option in q["options"]:
        print(option)

    user_answer = input("Your answer (A/B/C/D): ").strip().upper()

    if user_answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer is {q['answer']}.")

# Final Score
print("\n" + "-" * 40)
print(f"🎉 You scored {score} out of {len(questions)}.")

# Feedback
if score == len(questions):
    print("🏆 Excellent! You're a quiz master!")
elif score >= 3:
    print("👍 Good job!")
else:
    print("📘 Keep practicing!")
