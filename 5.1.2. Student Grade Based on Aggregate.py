# Write your code here...
# Input marks
a, b, c, d = map(int, input().split())

# Calculate total
total = a + b + c + d

# Calculate aggregate percentage
aggregate = total / 4

# Determine grade
if aggregate >= 75:
    grade = "Distinction"
elif 60 <= aggregate < 75:
    grade = "First Division"
elif 50 <= aggregate < 60:
    grade = "Second Division"
elif 40 <= aggregate < 50:
    grade = "Third Division"
else:
    grade = "Fail"

# Output results
print(total)
print(f"{aggregate:.2f}")
print(grade)
