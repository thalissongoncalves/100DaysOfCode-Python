student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇

for key in student_scores:
  values = student_scores[key]
  if values >= 91 and values <= 100:
    student_grades[key] = "Outstanding"
  if values >= 81 and values <= 90:
    student_grades[key] = "Exceeds Expectations"
  if values >= 71 and values <= 80:
    student_grades[key] = "Acceptable"
  if values <= 70:
    student_grades[key] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)