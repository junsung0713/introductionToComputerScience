import math
# Inputting the side lengths, first try
sideA = int(input('Length of side A?'))
sideB =int(input('Length of side B?'))
# Calculate third side via Pythagorean Theorem
hypotenuse = math.sqrt(sideA **2 + sideB ** 2)
print(hypotenuse)