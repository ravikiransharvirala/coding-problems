"""
Given a string find the following:

1. Reverse a string 
    - What are the test cases or limitations:
        - does it have special characters ? - do i need to remove the special characters
        - dealing with null values

2. Average length of the word
    - does it have special characters? - do i need to remove them

3. Return the number of times a given character appears in the string
    - check if the given string is not null
    - do i have to lower the string, to make it uniform




"""

def reverse_string(string):
    if not string:
        return None

    return str(string)[::-1]

def average_length(string):
    if not string:
        return None
    return sum([len(word) for word in string.split(" ")])/len(string.split(" "))

def character_count(string, target):
    if not string or not target:
        return None
    count = 0
    for c in str(string).lower():
        if target == c:
            count += 1
    return count


def cat_dog(str):
  cat_count = 0
  dog_count = 0
  for i in range(len(str)-2):
    if str[i:i+3] == "cat":
      cat_count += 1
    if str[i:i+3] == "dog":
      dog_count += 1
  return cat_count == dog_count






#string ="ravi"
#target = "i"

#print(reverse_string(string))
#print(average_length(string))

#print(character_count(string, target))
st = "catdog"

print(cat_dog(st))