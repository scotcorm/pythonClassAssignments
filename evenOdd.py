print("-------------")
print(" Even or Odd ")
print("-------------")

print('Enter a number and the program will tell us if it is "Even" or "Odd"')
print()

attempt_limit = 5
attempts = 0


while attempts < attempt_limit:
    number = input("What is your mystery number?  ")
    num = int(number)
    remainder = num % 2
    if num == 0:
        print("Goodbye!")
        break
    elif remainder == 0:
        print("Your number is even!")
    else:
        print("Your number is odd!")

    attempts += 1






