Age=int(input("please enter the age of the resident"))
sex=input("please enter the sex of the resident (women/man)")
if (Age >= 20 and sex=="man") or (Age >= 18 and Age  <= 35 and sex=="women"):
     print("the inhabitant is impossible")
else:
     print("the inhabitant is not impossible ")