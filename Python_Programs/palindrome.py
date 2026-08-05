from collections import deque

def palindrome_check(text):
    dq = deque()

    for ch in text:
        if ch.isalnum():
            dq.append(ch.lower())

    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False

    return True


text = input("Enter a String: ")

if palindrome_check(text):
    print("Palindrome")
else:
    print("Not Palindrome")
