bold="\033[1m"
end="\033[0m"

num1=int(input(bold+"Enter the first number:"+end))
num2=int(input(bold+"Enter the second number:"+end))

quotient=num1//num2
print("")
print(bold+"The quotient of two numbers is:"+end,quotient)