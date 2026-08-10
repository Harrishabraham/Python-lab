from collections import deque
while True:
    text = input("Enter a string: ")
    cleaned = ""
    for ch in text:
        if ch.isalnum():
            cleaned += ch.lower()
    dq = deque(cleaned)
    palindrome = True
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            palindrome = False
            break
    if palindrome:
        print("Palindrome")
    else:
        print("Not a Palindrome")
        break
