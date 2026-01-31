from time import sleep

text = input("Enter text: ")
ch = input("Enter a character: ")

count = 0
for c in text:
    if c == ch:
        count += 1

print("Occurrence:", count)
