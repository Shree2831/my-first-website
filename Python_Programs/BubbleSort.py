marks = [78, 92, 65, 88, 71, 95, 84]

print("SCHOOL RESULT PORTAL")

print("Original Marks :", marks)

n = len(marks)

for i in range(n - 1):
    for j in range(n - i - 1):
        if marks[j] > marks[j + 1]:
            marks[j], marks[j + 1] = marks[j + 1], marks[j]

    print("Pass", i + 1, ":", marks)

print()
print("\nFinal Result")

print("\nAscending Marks :", marks)
print()
print(" Marks sorted successfully")
print(" Ready to display on school portal")
