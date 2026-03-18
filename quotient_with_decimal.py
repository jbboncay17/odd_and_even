bold="\033[1m"
end="\033[0m"

num1=float(input(bold+"Enter the first number:"+end))
num2=float(input(bold+"Enter the second number:"+end))

if num2 !=0:
    quotient=num1/num2
    print("The quotient of the two numbers is:",quotient)
else:
    print("Cannot divide by zero")