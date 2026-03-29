import re, random
from colorama import Fore, init

init(autorest=true)
destination = {
    "beaches":["Bali","Maldives","phuket"],
    "mountains":["Swiss Alps","Rocky Mountains","Himalayas"],
    "cities":["Tokyo","New York","Paris"]


}
jokes = [
    "Why don't programmers like nature? Too many bugs!",

"Why did the computer go to the doctor? Because it had a virus!",

"Why do travelers always feel warm? Because of all their hot spots!"

def normalize_input(text):
    return re.sub(r"\s+"," ", text.strip().lower())
    