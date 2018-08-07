num1 = 10
num3 = 14
num4 = 12

#num1 = float(input("Enter first number: "))
#num2 = float(input("Enter second number: "))
#num3 = float(input("Enter third number: "))

if (num1 >= num3) and (num1 >= num4):
   largest = num1
elif (num3 >= num1) and (num3 >= num4):
   largest = num3
else:
   largest = num3

print("The largest number between",num1,",",num3,"and",num4,"is",largest)
