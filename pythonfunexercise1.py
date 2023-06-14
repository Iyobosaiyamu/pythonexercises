# # This will prompt the user to enter five test scores - doesn't prompt for error
# scores = []
# for i in range(5):
#     score = float(input("Enter test score between 0 and 100: "))
#     scores.append(score)

# # This part helps to calculate the average score 
# average_score = sum(scores) / len(scores)

# # This helps tp determine the score grade
# if average_score >= 90:
#     score_grade = "A"
# elif average_score >= 80:
#     score_grade = "B"
# elif average_score >= 70:
#     score_grade = "C"
# elif average_score >= 60:
#     score_grade = "D"
# else:
#     score_grade = "F"

# # This will print the average score and score grade
# print("Average Score:", average_score)
# print("Letter Grade:", score_grade)

# ---------------------------


def calculate_average_score(scores):
    total = sum(scores)
    average = total / len(scores)
    return average


def determine_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


# Prompt the user for five test scores
scores = []
for i in range(5):
    score = float(input("Enter test score between 0 and 100: "))
    while not (0 <= score <= 100):
        print("Invalid input. Please enter a score between 0 and 100.")
        score = float(input("Enter test score between 0 and 100: "))
    scores.append(score)

# Calculate the average score
average_score = calculate_average_score(scores)

# Determine the letter grade
letter_grade = determine_grade(average_score)

# Print the average score and letter grade
print("Average Score:", average_score)
print("Letter Grade:", letter_grade)
