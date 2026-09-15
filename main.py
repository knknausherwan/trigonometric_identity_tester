import math

# Value of x that will test the trigonometry rule
x = int(input("Enter test value: "))

# Trigonometry rule test
result = (math.cos(x)**2) + (math.sin(x)**2)

print(f"The result of the trigonometry rule with x being {x} is {result}")
