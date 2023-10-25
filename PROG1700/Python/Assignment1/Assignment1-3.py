print("Imperial to Metric Conversion")


numberOfTons = float(input("Enter the amount of tons: "))
numberOfStons = float(input("Enter the amount of stone: "))
numberOfPounds = float(input("Enter the amount of pounds: "))
numberOfOcunces = float(input("Enter the amount of ounces "))
 
totalOunces = 35840 * numberOfTons + 224 * numberOfStons + 16 * numberOfPounds + numberOfOcunces;
Kilos = totalOunces/35.274
metriTons = int(Kilos/1000)
totalKilos = int(Kilos-1000*metriTons)
totalGrams = round(((Kilos-metriTons*1000-totalKilos)*1000),1)
  
   
print(f"The metri weight is  {metriTons} metri tons {totalKilos} kilos, and  {totalGrams} grams");
