
print("====================")
print("     WELCOME")
print("====================")
while True:
    print("1.addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Modulus")
    print("6.Floor Division")
    print("7.Exit")
    choice = int(input("Enter your choice:"))
    if choice == 7:
        print("Thank you!")
        break
    if choice not in [1, 2, 3, 4, 5, 6]:
        print("Enter a valid choice!")
        continue
    num1 = int(input("Enter number1:"))
    num2 = int(input("Enter number2:"))
    if choice == 1:
        a = num1 + num2
        print("Addition:", a)
        print()
    elif choice == 2:
        s = num1 - num2
        print("Subtraction:", s)
        print()
    elif choice == 3:
        m = num1 * num2
        print("Product:", m)
        print()
    elif choice == 4:
        if num2 == 0:
            print("Error! ZeroDivision Error")
        else:
            d = num1 / num2
            print("Division:", d)
            print()
    elif choice == 5:
        if num2 == 0:
            print("Error!")
        else:
            m = num1 % num2
            print("Modulus:", m)
            print()
    elif choice == 6:
        if num2 == 0:
            print("Error!")
        else:
            f = num1 // num2
            print("Floor division:", f)
            print()
print("==============")
