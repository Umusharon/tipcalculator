foodprice=input("enter price for the food:")
taxprice=int(foodprice)*9/100
tipprice=int(foodprice)*18/100
grandtoatal=int(foodprice)+taxprice+tipprice
print(f"food price={foodprice}$")
print(f"tax price={taxprice}$")
print(f"tip price={tipprice}$")
print(f"grand total={grandtoatal}$")