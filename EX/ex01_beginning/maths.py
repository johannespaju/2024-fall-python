"""EX01 Maths."""

"""
Find the average of a, b, c and d, but first the numbers must be multiplied. a multiplied by 1, b multiplied by 2,
c multiplied by 3 and d multiplied by 4.
After the multiplication find the average of the numbers and print it out.
 """
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
d = int(input("Enter the value of d: "))
print((a * 1 + b * 2 + c * 3 + d * 4) / 4)

"""
Calculate the sum of two fractions.

One fraction is x/y where x and y are numbers given as input.
The other fraction is u/t where u and t are also numbers given as input.

Find and print the sum of x/y + u/t.

NB! the fraction does not have to be in the simplest form.
NB! the answer should be given as a string and should not contain any commas.
"""

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
u = int(input("Enter the value of u: "))
t = int(input("Enter the value of t: "))

print(f"{x * t + u * y}/{y * t}")

"""
Calculate and print how many hours are needed per week with given ECTS and amount of weeks, if each ECTS is 26 hours.

If it is not possible, print out -1.

Example 1
ects = 30
weeks = 12

Output
65

Example 2
ects = 1
weeks = 1

output
26

Example 3
ects = 1
weeks = 0

output
-1
"""
ects = int(input("Enter the amount of ECTS: "))
weeks = int(input("Enter the number of weeks: "))
hours = int(ects * 26)

if weeks == 0:
    print(-1)

else:
    hours_per_week = hours / weeks

    if hours_per_week > 168:
        print(-1)

    else:
        print(hours_per_week)
