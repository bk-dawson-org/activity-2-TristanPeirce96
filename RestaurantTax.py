price = float(input("Entre the price of the food before tax: "))
tax = (15/100)
pricetaxincluded = ((price * tax) + price)
print("The price with tax is: $", pricetaxincluded)

def calculatearea(radius):
    area = 3.14 * radius**2
    return area

circle1 = calculatearea(3)
print(circle1)