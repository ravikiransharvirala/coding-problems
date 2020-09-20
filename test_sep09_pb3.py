'''
Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string



["the", " ","sky" "is" "blue"]

nput_list.reverse()

stack.push()
if word != " ":
    stack.push(word)

output = ""

while len(stack) > 1:
    output = output+stack.pop()+" "

blue is sky the.

for e in input_list:

'''

def reverse_string(input):
    if not input:
        return None
    stack = []
    input_list = input.split(" ")
    for word in input_list:
        if word != " ":
            stack.append(word)
    
    output = ""
    while len(stack) > 1:
        output = output+str(stack.pop())+" "
    
    output = output+stack.pop()
    return output

test = ""

print(reverse_string(test))