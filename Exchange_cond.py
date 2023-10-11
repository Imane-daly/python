A=int(input("please enter the value of A:"))
B=int(input("please enter the value of B:"))
if A * B > 0:
    C=A
    A=B
    B=C
else:
    C = A + B
    D = A * B
    A = B
    B = D 
    print("the new value of A is:",A)
    print("the new value of B is:",B)
