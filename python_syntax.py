# Python syntax 语法

# print absolute value of an integer
a = 100
if a >= 0:
    print(a)
else:
    print(-a)

# print if the input age is adult or not
year = input("Please enter your birth year: ")

print(2020 - int(year))

a = int(2020 - int(year))
if a >= 18:
    print("Adult")
else:
    print("underage")

# print what to do next
condition = input("What can I help you with?")

if condition == "hungry":
    print("Please eat.")
elif condition == "tired":
    print("Get some rest.")
elif condition == "sick":
    print("Go to a doctor.")
elif condition == "chill":
    print("Go to study.")
else:
    print("Sorry, I don\'t understand \"your condition\".")

print('I\'m learning\nPython.')

print('\\\n\\')

print('\\\t\\')

print(r'\\\t\\')

print('''line1
line2
line3''')

# -*- coding: utf-8 -*-
print(r'''hello,\n
world''')

True

False

3 > 2

3 > 5

