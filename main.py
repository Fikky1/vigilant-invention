# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from itertools import count
from types import new_class


def read_file_content(filename):
    # [assignment] Add your code here 
    with open("./story.txt") as openfile:
        read_file = open_file.read()
     print(read_file)
     new+read_file.split()
     print(new_class)
        


def count_words():
    text = readfile("./story.txt")
    # [assignment] Add your code here
    split_text = text.split()
    print(split_text)
    count ={}
    for i in split_text:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count
print(count_words())

    