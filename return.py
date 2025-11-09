age = int(input("Enter your age"))
def eligible_to_vote(age):
    if(age>=18):
        return "you are eligible to vote"
    else:
        return "you are not eligible to vote"
    

print(eligible_to_vote(age))


          