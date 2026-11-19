rows = int(input("Please enter the total number of rows:"))
if row%2 == 0:
     halfDiamRow = int(row/2)
else:
halfDiamRow = int(row/2)+1
space = halfDiamRow-1

for i in range (1, halfDiamRow +1):
     for j in range(1, space+1):
          print(end="")
    space = space-1
num=1
