
import math

side_a = float(input("Side a (metres): "))
side_b = float(input("Side b (metres): "))

if side_a <= 0:
    print("Side a must be greater than zero.")
elif side_b <= 0:
    print("Side b must be greater than zero.")
else:
    hypotenuse = math.sqrt(side_a ** 2 + side_b ** 2)
    print("The hypotenuse is: {:.2f} metres".format(hypotenuse))

    
