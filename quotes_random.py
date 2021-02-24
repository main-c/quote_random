# -*- coding: utf8 -*-

from random import*
import json

def read_values_from_json(file , key):
    # Create a new empty list
    values = []
    # open a json file with my objects
    with open(file) as f:
        # load all the data contained in this file
        data = json.load(f)
    for entry in data:
        # add each item in my list
        values.append(entry[key])

    return values

def clean_string(sentences):
    cleaned = []
      # Store quotes on a list. Create an empty list and add each sentence one by one.
    for sentence in sentences:
        # Clean quotes from whitespace and so on
        clean_sentence = sentence.strip()
        clean_sentence = clean_sentence.capitalize()
        # don't use extend as it adds each letter one by one!
        cleaned.append(clean_sentence)
    return cleaned

# Return a random item from a list
def get_random_item_in(object_list, random_number=-1):
    if random_number == -1:
        random_number = randrange(len(object_list)-1)
    item = object_list[random_number]
    return item, random_number

# Return a random value from a json file
def random_value(file_name, item_name):
    all_values = read_values_from_json(file_name, item_name)
   # all_values = clean_string(all_values)
    return get_random_item_in(all_values)

def print_random_sentence():
    rand_quote = random_value("quote.json", "quote")
    rand_author = random_value("author.json", "author")
    print("{0} a dit : <<{1}>>".format(rand_author, rand_quote))

def mainloop():
    user_answer = ""
    while True:
        user_answer = input("Appuyer une touche pour afficher une nouvelle citaion ou entrer B pour quitter")
        if user_answer.upper() != "B":
          print_random_sentence()
    else:
        exit()


if __name__ == '__main__':
    mainloop()