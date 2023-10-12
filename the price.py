PHT=float(input("please enter the product price excluding tax:"))
Cat=input("please enter product category:")
if Cat =="A":
    print("the price TTC the product is:",PHT+PHT*0.07)
elif Cat =="B":
    print("the price TTC the product is:",PHT+PHT*0.2)
elif Cat =="C":
    print("the price TTC the product is:",PHT+PHT*0.25)
else :
    print("Category does not exist")