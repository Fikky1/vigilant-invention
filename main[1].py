# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from graphlib import TopologicalSorter
from operator import truediv
from socket import if_indextoname


def find_anagram(str1, str2):
#[assignment] Add your code here
    str1 = "tools"
    str2 = "stool"
    str1_anagram = sorted(str1)
    str2_anagram = sorted(str2)

    if sorted (str1) == sorted (str2) :
       return True
    else:
     return False
print(find_anagram("tools", "stool"))
    

    

