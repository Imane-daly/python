age=int(input("please enter the age of the resident:"))
sexe=input("please enter the sexe of the resident(femme/homme):")
if (age >= 20 and sexe == "homme") or (age >= 18 and age <= 35 and sexe == "femme"):
    print("the inhabitant is impossible")
else:
    print("the inhabitant and not impossible")