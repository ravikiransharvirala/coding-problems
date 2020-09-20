"""
[Python] Powerful Ultimate Binary Search Template. Solved many problems
link - https://leetcode.com/discuss/general-discussion/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems

>> Most generalized binary search

Minimize k , s.t. condition(k) is True
"""
def binary_search(array):
    def condition(value):
        pass

    left, right = min(array), max(array)
    while left < right:
        mid = left+(right-left)//2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left

def mySqrt(x):
    left, right = 0, x+1
    while left < right:
        mid = left + (right-left)//2
        if mid * mid > x:
            right = mid
        else:
            left = mid + 1
    return left - 1

def search_insert_postion(nums, target):
    """
    Sample test case:
    Input: [1,3,5,6], 5
    """
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right-left)//2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left


#print(mySqrt(32))
print(search_insert_postion([1,3,5,6], 2))

