"""EX01 ATM."""

"""
pmst summa /100 + jääk/50 + jääk/20 etc.
Create a machine that dispenses money using 1€, 5€, 10€, 20€, 50€ and 100€ banknotes.

Given the sum, one must print out how many banknotes does it take to cover the sum. Task is to cover the sum with as little
banknotes as possible.

Example
The sum is 72€
We use four banknotes to cover it. The banknotes are 20€, 50€, 1€ and 1€.
"""

amount = int(input("Enter a sum: "))

number_of_100 = amount // 100
leftover_100 = amount % 100

number_of_50 = leftover_100 // 50
leftover_50 = leftover_100 % 50

number_of_20 = leftover_50 // 20
leftover_20 = leftover_50 % 20

number_of_10 = leftover_20 // 10
leftover_10 = leftover_20 % 10

number_of_5 = leftover_10 // 5
leftover_5 = leftover_10 % 5

number_of_1 = leftover_5 // 1

banknotes = number_of_100 + number_of_50 + number_of_20 + number_of_10 + number_of_5 + number_of_1
print(f"Amount of banknotes needed: {banknotes}")
