name = input("please enter your name: ")
distance = input("please enter the distance in kilometers for delivery: ")
recost = input("Enter the cost of cost of records purchased: ")

deliveryCost = float(distance)*15
recordCost = float(recost)* 1.14
totalCost = float(deliveryCost + recordCost)

print("purchase summary for " + name)
print("Delivery Cost: " + str(round(deliveryCost,2)))
print("purchase cost: "+  str(round(recordCost,2)))
print("Total Cost:    "  + str(round(totalCost,2)))