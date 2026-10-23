# HCF

num1 = int(input("enter first number: "))

num2 = int(input("enter second number: "))

if num1 < num2:
    factor = num1
else:
    factor = num2
    
while num1 % factor != 0 or num2 % factor != 0:
    factor -= 1
    
print("HCF is:", factor)

    
