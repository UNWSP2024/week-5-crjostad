import random

num1 = random.randint(1, 500)
num2 = random.randint(1, 500)

print(num1)
print("  +")
print(num2)


answer = int(input("Enter answer: "))

if answer == num1 + num2:
    print("Congratulations")

if answer != num1 + num2:
    print("You are incorrect the answer is", num1 + num2)
