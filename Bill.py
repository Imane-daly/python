N=int(input("please enter the number of copies"))
if N <= 10:
    F = N * 0,30
elif N <=30:
        F = 10 * 0,30 +(N - 10)*0,25
else:
    F = 10 * 0,30 + 20 * 0,25 +(N - 30)* 0,2