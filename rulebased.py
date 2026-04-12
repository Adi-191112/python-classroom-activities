import re
import random

destination = {
    "beaches":["Bali","Maldives","phuket"],
    "mountains":["Swiss Alps","Rocky Mountains","Himalayas"],
    "cities":["Tokyo","New York","Paris"]


}
jokes = [
    "Why don't programmers like nature? Too many bugs!",

"Why did the computer go to the doctor? Because it had a virus!",

"Why do travelers always feel warm? Because of all their hot spots!"]

def normalize_input(text):
    return re.sub(r"\s+"," ", text.strip().lower())


def recommend():
   print ("TravelBot: Beaches, mountains, or cities?")

   preference = input("you: ")
   preference = normalize_input(preference)


   if preference in destination:
       suggestion = random.choice(destination[preference])

       print(f"TravelBot: How about {suggestion}?")
       print("TravelBot: Do you like it? (yes/no)")
       answer = input("you: ").lower()


       if answer == "yes":
           print(f"TravelBot: Awsome! Enjoy {suggestion}!")
        


       elif answer == "no":
           print("TravelBot: Lets try another.")
           recommend()
       else:
           print("TravelBot: i will suggest again.")
           recommend()

   else:
       print("TravelBot: Sorry; i do not have that type of destination.")
       recommend()
       
def show_help():
    print("\nI can:")
    print("- suggest travel spots(say ´recommendation´)")


def chat():
    print("Hello! I´m TravelBot.")
    name = input("your name? ")
    print(f"nice to meet you, {name}!")

    show_help()

    while True:
      user_input = input(f"{name}:")
      user_input = normalize_input(user_input)

      if "recommend" in user_input:
          recommend()


      elif "exit" in user_input:
          break
      

      else:
          print("TravelBot; could you rephrase?")

    
if __name__ == "__main__":
    chat()