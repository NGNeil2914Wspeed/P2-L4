from time import sleep

def getint(question):
    while True:
        try:
            a = int(input(question))
            return a
        except ValueError as e:
            print (f"{e}\nPlease enter a whole number")

name = input("hey im gonna help you do some maths stuffbut first, whats your name? ")

sum = 0
digit = 0
temp = getint(f"{name} please enter your number: ")
num = temp
while temp>0:
    digit = temp%10
    sum+=digit**3
    temp //= 10

if num == sum:
    print ("Is an armstrong number")
else:
    print ("Not an armstrong number")