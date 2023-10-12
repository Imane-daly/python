while True :
    n=int(input("please enter the value of n"))
    if n >= 0:
        break
if n == 0:
    print("the factoriel of 0 is 1")
else:
    F = 1
    for i in range(2,n+1):
        F = F*i
    print("the factoriel of",n,"is:",F)