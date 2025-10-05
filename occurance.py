word = input("Enter the word")
letter = input("Enter the letter")
i = 0
count = 0
while(i < len(word)):
    if(word[i] == (letter)):
        count = count + 1 
    
    i = i + 1

    

print("The count is: ", count)    