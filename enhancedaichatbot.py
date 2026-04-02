print("Welcome to AI Chatbot, please enter your name")
name = input()
print(f"it is a pleasure to meet you {name}")
print("how are you feeling today good/bad")
mood = input().lower()
if(mood == "good"):
    print("i am very happy to know that")

elif(mood == "bad"):
    print("dont worry you will feel better soon")

else:
    print("sometimes it is hard to put feelings into words")

