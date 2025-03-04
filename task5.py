# 1. Check a given number is positive, negative, or zero:
num = input("Enter a number")
if num > 0:
    print(num, "is positive")
elif num < 0:
    print(num, "is negative")
else:
    print(num, "is equal to zero")

print("Time Complexity:", "O(1)")
print("Space Complexity:", "O(1)")

# ---------------------------------------------------------------------------

# 2. Determine if a number is odd or even:

num = input("Enter a number")
if num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

print("Time Complexity:", "O(1)")
print("Space Complexity:", "O(1)")

# --------------------------------------------------------------------------

# 3. Check if a person is eligible to vote (age>=18):

age = input("Enter the age")
result = "Eligible to vote" if age>=18 else "Not Eligible to vote"
print(result)
print("Time Complexity:", "O(1)")
print("Space Complexity:", "O(1)")
# ----------------------------------------------------------------------------------

# 4. find the greatest of two numbers

num1 = input("Enter first number")
num2 = input("Enter second number")
result = "num1 is greater" if num1>num2 else "num2 is greater"
print(result)
print("Time Complexity:", "O(1)")
print("Space Complexity:", "O(1)")

# ----------------------------------------------------------------------------------

# 5. print pass if a student scores more than 40 marks. Otherwise, print "Fail":

marks = input("Enter the marks")
if marks>'40':
    print("Pass")
else:
    print("Fail")
print("Time Complexity:", "O(1)")
print("Space Complexity:", "O(1)")

# ----------------------------------------------------------------------------------

# 6. Write a program to display the day of the week based on a number input (1 for Monday, 2 for Tuesday etc)

number = input("Enter a number")
if number == '1':
    print("Monday")
elif number == '2':
    print("Tuesday")
elif number == '3':
    print("Wednesday")
elif number == '4':
    print("Thursday")
elif number == '5':
    print("Friday")
elif number == '6':
    print("Saturday")
elif number == '7':
    print("Sunday")
else:
    print("Not valid")
print("Time Complexity:", "O(1)")
print("Space Complexity:", "O(1)")

# ----------------------------------------------------------------------------------

# 7. Implement a simple calculator to perform addition, subtraction, multiplication, and division:

num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
inp = input("Enter an operation").lower()
if inp in ['add', '+']:
    print(num1+num2)
elif inp in ['sub', '-']:
    print(num1-num2)
elif inp in ['mul', '*']:
    print(num1*num2)
elif inp in ['div', '/']:
    if num2 == 0:
        print("Div with 0 is not possible")
    else:
        print(num1/num2)
else:
    print("Invalid Input")

print("Time Complexity:", "O(1)")
print("Space Complexity:", "O(1)")

# ----------------------------------------------------------------------------------

# 8. program to display the name of a month based on the month number:

month = int(input("Enter a number"))
if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")

print("Time Complexity:", "O(1)")
print("Space Complexity:", "O(1)")

# ----------------------------------------------------------------------------------

# 9. Write a program to find the greatest of three numbers:

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter third number"))
if num1 > num2 and num1 > num3:
    print(num1, "is greater number")
elif num2>num1 and num2 > num3:
    print(num2, "is greater number")
elif num3 > num1 and num3 > num2:
    print(num3, "is greater")
else:
    print("All three are equal numbers")

print("Time Complexity:", "O(1)")
print("Space Complexity:", "O(1)")

# ----------------------------------------------------------------------------------

# 10. check if a year is leap or not:

year = int(input("Enter a year"))
if ((year % 4 == 0) and (year % 100 != 0)) or ((year % 400 == 0) and (year % 100 == 0)):
    print("Leap Year")
else:
    print("Not a Leap year")
print("Time Complexity:", "O(1)")
print("Space Complexity:", "O(1)")

# ----------------------------------------------------------------------------------

#  11. classify a character entered by the user as a vowel, consonant, or neither:

def alphabet(char):
    vowels = "aeiouAEIOU"
    if char.isalpha():
        if char in vowels:
            return "Vowel"
        else:
            return "Consonant"
    else:
        return "neither"
    
char = input("Enter a single character")
if len(char) == 1:
    result =alphabet(char)
    print(result)
else:
    print("Enter single character only")
print("Time Complexity:", "O(1)")
print("Space Complexity:", "O(1)")

# ----------------------------------------------------------------------------------

# 12. grade of a student based on the marks they score:

marks = int(input("Enter marks"))
if marks >= 90 and marks <=100:
    print("Grade A")
elif marks >= 80 and marks <=89:
    print("Grade B")
elif marks >= 70 and marks <=79:
    print("Grade C")
elif marks < 70:
    print("Fail")
else:
    print("Not a number")
print("Time Complexity:", "O(1)")
print("Space Complexity:", "O(1)")

# ----------------------------------------------------------------------------------

# 13. Write a program to check if three sides length form a valid triangle:

a = int(input("Enter the length of side 1: "))
b = int(input("Enter the length of side 2: "))
c = int(input("Enter the length of side 3: "))
if (a+b) > c and (b+c) > a and (a+c) > b:
    print("It will form a valid triangle")
else:
    print("It will not form a valid triangle")
print("Time Complexity:", "O(1)")
print("Space Complexity:", "O(1)")

# ----------------------------------------------------------------------------------------------------

# 14. print all numbers 1 to 100 using for loop:

for i in range(1, 101):
    print(i)

print("Time Complexity:", "O(n)")
print("Space Complexity:", "O(1)")

# --------------------------------------------------------------------------------------------

# 15. Write a program to print the sum of the first n natural numbers. (n*n+1/ 2)

n = 50
print((n*(n+1))/2)
def func(n):
    print((int)(n*(n+1)/2))

func(50)
print("Time Complexity:", "O(1)")
print("Space Complexity:", "O(1)")

# -------------------------------------------------------------------------------------------

# 16. print all even numbers between 1 and 50 using a while loop:

i = 1
while i <= 50:
    if i % 2 == 0:
        print(i)
    i+=1
print("Time Complexity:", "O(n)")
print("Space Complexity:", "O(1)")

# --------------------------------------------------------------------------------------------

# 17. Display the multiplication table of a given number

num = int(input("Enter a number"))
for i in range(1, 11):
    print(num, "*", i, "=", (num*i))

print("Time Complexity:", "O(1)")
print("Space Complexity:", "O(1)")

# ----------------------------------------------------------------------------------------------------

# 18. Reverse a number using a while loop.
#   1. also we get the sum of all the digits

num = 54327
rev = 0
sum = 0
while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10
    sum += rem
print(rev)
print(sum)

print("Time Complexity:", "O(logn)")
print("Space Complexity:", "O(1)")

# -------------------------------------------------------------------------------------------------

# 19. program to count the number of digits in a given number using a while loop:

num = 12345
count = 0
while num > 0:
    rem = num % 10
    count += 1
    num = num // 10

print(count)

print("Time Complexity:", "O(logn)")
print("Space Complexity:", "O(1)")

# -----------------------------------------------------------------------------------------------------------

# 20. Write a program that keeps asking the user to enter numbers until they enter a negative number. Use a while loop.

while True:
    number = int(input("Enter a number"))
    if number < 0:
        break

num1 = 0
while num1 >= 0:
    num1 = int(input("Enter non negative number only"))

print("Time Complexity:", "O(k+m)")
print("Space Complexity:", "O(1)")