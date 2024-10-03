import random

def quiz_numbers():
    num1 = random.randint(1, 500)
    num2 = random.randint(1, 500)
    return num1, num2

def check_answer(num1, num2, answer):
    if answer == num1 + num2:
        print("Congratulations")
    else:
        print("You are incorrect the answer is", num1 + num2)

num1, num2 = quiz_numbers()

print(num1)
print("  +")
print(num2)
print("___")
answer = int(input("Enter answer: "))
check_answer(num1, num2, answer)
