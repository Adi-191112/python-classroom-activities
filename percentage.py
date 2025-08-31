# creating user input
print("Enter your marks")
math = int(input("Enter your math marks: "))
english = int(input("Enter your english marks: "))
science = int(input("Enter your science marks: "))   
sports = int(input("Enter your sports marks: "))         
sum =math + english + science + sports
percentage =int( (sum/400)*100)
print("your percentage is ", percentage)
