control = str(input("Enter yes to loop or no to exit:  "))
x = 0
while control == "yes":
  itemquantity = float(input("Enter item quantity:   "))
  itemprice = float(input("Enter the price of each item:    "))
  extendedprice = itemquantity * itemprice

  if extendedprice > 10000:
    discount = extendedprice * 0.25
  else:
    discount = extendedprice * 0.10

  total = extendedprice - discount

x = x + 1

print("The extended price is $", extendedprice, " with a discount of $", discount, " and a total of $", total)

control = str(input("Enter yes to loop or no to exit:  "))
print("You have ordered", x, "items")