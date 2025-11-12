a = input("enter a number")
b = input("enter a number")
if a % 2 == 0 and b % 2 == 0:
    print("Both numbers are even.")
elif a % 2 != 0 and b % 2 != 0:
    print("Both numbers are odd.")
elif a % 2 == 0 and b % 2 != 0:
    print("First number is even and second number is odd.")
else:
    print("First number is odd and second number is even.")
