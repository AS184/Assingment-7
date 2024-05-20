start = 1
stop = 25
while start <= stop:
  odd = start % 2
  if odd != 0: # != means not, == means equal
    print(start)
  start = start +1