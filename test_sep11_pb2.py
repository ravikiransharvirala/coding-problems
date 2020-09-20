"""



Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

[2, 5, 6]

for num in nums2:
    for n in nums1:
        if num

1st

num = 2
n = 3
if num < n:



"""

def solution(nums1, nums2):
    indx1 = 0
    indx2 = 0
    result = []
    
    while indx1 < len(nums1) and indx2 < len(nums2):
        if nums1[indx1] < nums2[indx2]:
            result.append(nums1[indx1])
            indx1 += 1
        elif nums1[indx1] > nums2[indx2]:
            result.append(nums2[indx2])
            indx2 += 1
        else:
            result.append(nums1[indx1])
            result.append(nums2[indx2])
            indx1 += 1
            indx2 += 1
    
    while indx1 < len(nums1):
        result.append(nums1[indx1])
        indx1 += 1
    
    while indx2 < len(nums2):
        result.append(nums2[indx2])
        indx2 += 1
    return result

nums1 = [1,2,3]
nums2 = [2,5,6]


def solution2(lst1, lst2):
    indx1 = 0
    indx2 = 0

    while indx1 < len(lst1) and indx2 < len(lst2):
        if lst1[indx1] < lst2[indx2]:
             

print(solution(nums1, nums2))

