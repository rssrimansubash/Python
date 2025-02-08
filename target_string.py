import string
import random
import time

letters = string.ascii_letters
target = input("Enter Target String : ")
result = ""

for letter in target:
    while True:
        r = random.choice(letters)
        print(result + r)
        if r == letter:
            result += r
            break
        time.sleep(0.01)

print("Final Result : ", result)
