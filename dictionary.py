# This python program is the implementation of a interactive dictionary
#
# Its features include:
#
# 1. The program interacts with users using command line.
#
# 2. It tolerates minor typos. (Give you a prompt by showing a similar word)
#
# 3. It is capable of handling inputs of upper cases.

import json
from difflib import get_close_matches

# Import data
data = json.load(open("data.json"))

# Translate function
def translate(key_word):
    if key_word in data:
        return data[key_word]
    elif key_word.title() in data:        # Handle titles
        return data[key_word.title()]
    elif key_word.upper() in data:        # Handle acronym
        return data[key_word.upper()]
    elif get_close_matches(key_word, data.keys()):
        sw = get_close_matches(key_word,data.keys())[0]    # find the word with highest similarity
        yn = input("Do you mean %s instead? Enter Y if yes, or N if no: " % sw).lower()
        while True:
            if yn == "y":
                return translate(sw)
            elif yn == "n":
                return "The word doesn't exist! Please try again!"
            else:
                yn = input("We don't understand your input. Please try again: ").lower()
    else:
        return "The word doesn't exist! Please try again!"

result = translate(input("Enter your word: ").lower())

cnt = 0;

if type(result) == list:
    for item in result:
        cnt += 1
        print("Definition "+str(cnt)+": "+ item)
else:
    print(result)
