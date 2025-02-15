"""EX01 Hello."""

print("What is your name?")
# ask for name
name = input()
# print introduction

print("Hello, " + name + "! Enter a random number:")
# ask for number 1 input'

num1 = int(input())

print("Great! Now enter a second random number:")

num2 = int(input())

answer = num1 + num2
print(f"{num1} + {num2} is {answer}")
