control = str(input("Enter yes to loop or no to exit:  "))
x = 0
total_pay = 0
while control == "yes":
  name = str(input("Enter your name:   "))
  hours_worked = float(input("Enter the number of hours you work:    "))
  rate_of_pay = float(input("Enter your pay rate:    "))
  if hours_worked <= 40:
    gross_pay = hours_worked * rate_of_pay
  else:
    gross_pay = (40 * rate_of_pay) + ((hours_worked - 40)) * 1.5 * rate_of_pay
    print(name, "has a gross pay of $", gross_pay)

  total_pay = total_pay + gross_pay
  x = x + 1
  
  control = str(input("Enter yes to loop or no to exit:  "))
  print("You have looped", x, "times")
  averagepay = total_pay / x # x = employee number
  print("The average pay is $", averagepay)