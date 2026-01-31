from time import sleep

def getint(question):
    while True:
        try:
            a = int(input(question))
            return a
        except ValueError as e:
            print (f"{e}\nPlease enter a whole number")

n = int(input("Enter a decimal number: "))

binary = ""

while n > 0:
    binary = str(n % 2) + binary
    n = n // 2

print("Binary:", binary)
