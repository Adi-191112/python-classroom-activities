ch = input("Enter a character")
# OR AND 
if(len(ch) == 1):

  if((ord(ch) >= 65 and ord(ch)<= 90) or (ord(ch) >= 97 and ord(ch) <= 122) ):
    print("Alphabet")

  else:
    print("Not an Alphabet")


else:
  print("Enter a proper character")