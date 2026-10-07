def linear_search(roll_numbers, target):
    for i in range(len(roll_numbers)):
        if roll_numbers[i] == target:
            return i
    return -1


def binary_search(roll_numbers, target):
    low = 0
    high = len(roll_numbers) - 1

    while low <= high:
        mid = (low + high) // 2

        if roll_numbers[mid] == target:
            return mid
        elif roll_numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1



registered_students = [102, 115, 121, 134, 148, 156, 167, 179, 185, 196]


print(" EXAM REGISTRATION VERIFICATION")


print("Registered Roll Numbers:", registered_students)

roll = int(input("\nEnter your Roll Number: "))


linear_result = linear_search(registered_students, roll)


sorted_students = sorted(registered_students)
binary_result = binary_search(sorted_students, roll)

print("\n------------- SEARCH RESULTS ------------")

if linear_result != -1:
    print("Linear Search  : Roll No.", roll, "is REGISTERED")
else:
    print("Linear Search  : Roll No.", roll, "is NOT REGISTERED")

if binary_result != -1:
    print("Binary Search  : Roll No.", roll, "is REGISTERED")
else:
    print("Binary Search  : Roll No.", roll, "is NOT REGISTERED")


print("Verification Completed Successfully!")
