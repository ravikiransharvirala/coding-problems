"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4



"""

def solution(input):
    if not input:
        return None
    arr_dict = {}
    for num in input:
        if num in arr_dict:
            arr_dict[num] += 1
        else:
            arr_dict[num] = 1
    for e in arr_dict.keys():
        if arr_dict[e] == 1:
            return e
    return None


input = [4,1,2,1,2]
print(solution(input))