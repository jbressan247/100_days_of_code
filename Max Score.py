# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
max_scores = 0
min_scores = 100

for max_score in student_scores:
    if max_score > max_scores:
        max_scores = max_score

for min_score in student_scores:
    if min_score < min_scores:
        min_scores = min_score

print(f"The highest score in the class is: {max_scores}")
print(f"The lowest score in the class is: {min_scores}")
