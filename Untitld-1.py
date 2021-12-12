a = input()
b = [int(x) for x in a.split()]
x = (b[0] + b[-1]) / 2
for i in b:
     if i > x:
          print(i, sep='')
