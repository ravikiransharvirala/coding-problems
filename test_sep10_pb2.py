"""



Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 105
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


1st iteration

[2,7,11,15] 9

2: 0, 7:1, 11:2,  



9-2 in nums


[3,2,4] 6

1st

6-3 in nums:

2nd

6-2 = 4 in

"""

def target_indices(nums, target):
    if not nums:
        return None
    for num in nums:
        if (target-num) in nums:
            if nums.index(num) != nums.index(target-num):
                return [nums.index(num), nums.index(target-num)]
    return None

def target_indices_2(nums, target):
    nums_hashmap = {}
    for i, v in iterator(nums):
        nums_hashmap[v] = i
    
    for i in range(len(nums)):
        if target - nums[i] in nums_hashmap and i!= nums_hashmap[target-nums[i]]:
            return (i, nums_hashmap[target-nums[i]]

def target3(nums, target):
    if not nums or not target:
        return None
    
    visted = {}

    for i in range(len(nums)):
        if target-nums[i] in visted:
            return (i, visted[target-nums[i]])
        visted[nums[i]] = i 
    return False