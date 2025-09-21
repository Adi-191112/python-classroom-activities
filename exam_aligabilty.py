medical_cause = (input("did you have a medical cause Y or N "))
a = int(input("enter your attendance"))
if(medical_cause == "Y"):
    print("yes you are allowed")
else:
    if(a > 75):
        print("you are allowed")
    
    else:
        print("you are not allowed")

