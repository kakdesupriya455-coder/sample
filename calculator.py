num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
obtained = float(input("Enter obtained marks: "))
total = float(input("Enter total marks: "))

print("1.Add")
print("2.Subtract")
print("3.multiplication")
print("4.Division")
print("5.Percentage")
choice = input("Choose: ")

if choice == "1":
    print("Answer:", num1 + num2)

elif choice == "2":
    print("Answer:", num1 - num2)

elif choice == "3":
    print("Answer: ", num1 * num2 )

elif choice == "4":
    print("Answer: ", num1 / num2)

elif choice == "5":

    percentage = (obtained / total) * 100
    print("Percentage =", percentage, "%")
    
  
else:
    print("Invalid Choice")