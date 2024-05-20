control = str(input("Enter yes to loop or no to exit:  "))
x = 0
while control == "yes":
  name = str(input("Enter your name:   "))
  exam_one = float(input("Enter your first exam score:    "))
  exam_two = float(input("Enter your second exam score:    "))
  average = (exam_one + exam_two) / 2
  print(name, "has an average of ", average)
  x = x + 1
  control = str(input("Enter yes to loop or no to exit:  "))
  print("You have looped", x, "times")