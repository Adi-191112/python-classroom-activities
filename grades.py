m = int(input("enter your maths marks"))
s = int(input("enter your science marks"))
e = int(input("enter you english marks"))
g = int(input("enter your geography marks"))
avg =( m+s+e+g )/4
print("the average is ", avg)
if(avg>=91 and avg<=100):
    print("your grade is 1")
elif(avg>=81 and avg<=90):
    print("your grade is 2")
elif(avg>=71 and avg<=80):
    print("your grade is 3")
elif(avg>=61 and avg<=70):
    print("your grade is 4")
else:
    print("failed")