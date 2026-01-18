#SWAPPING NUMBERS
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
#WITHOUT USING THIRD VARIABLE
a=a+b
b=a-b
a=a-b
c=int(input("Enter third number:"))
d=int(input("Enter fourth number:"))
#USING THIRD VARIABLE
temp=c
c=d
d=temp
print("After swapping without third variable:")
print("First number:",a)
print("Second number:",b)
print("After swapping using third variable:")
print("Third number:",c)
print("Fourth number:",d)
