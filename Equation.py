import math 
a=float(input("please enter the value of a:"))
b=float(input("please enter the value of b:"))
c=float(input("please enter the value of c:"))
d = (b**2) - 4 * a * c 
if d < 0 :
    print("No real solution:")
elif d == 0 :
      x = (-b) / (2 * a)
      print("the solution is:",X)
else :
    x1 = (-b -math.sqrt(d)) / (2*a)
    x2 = (-b +math.sqrt(d)) / (2*a)
    print("the solutions are:",format(x1,".2f"), "et",format(x2,".2f"))