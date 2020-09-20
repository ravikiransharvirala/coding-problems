"""
Input : a = {{1, 3, 4}, {5, 2, 9}, {8, 7, 6}}
Output : 7
There are total 7 elements min elements are 1, 2, 6 and 4. And max elements are 9, 8 and 7.

Input : a = {{1, 1}, {1, 1}, {1, 1}}
Output : 6


"""

def postional_elements(nums):
    pos_elem_set = set()
    for i in range(len(nums)):
        rowmin = float('inf')
        rowmax = float('-inf')
        for j in range(len(nums[0])):
            if nums[i][j] < rowmin:
                rowmin = nums[i][j]
            if nums[i][j] > rowmax:
                rowmax = nums[i][j]
        pos_elem_set.add(rowmin)
        pos_elem_set.add(rowmax)
    
    for j in range(len(nums[0])):
        colmin = float('inf')
        colmax = float('-inf')
        for i in range(len(nums)):
            if nums[i][j] < colmin:
                colmin = nums[i][j]
            if nums[i][j] > colmax:
                colmax = nums[i][j]
        pos_elem_set.add(colmin)
        pos_elem_set.add(colmax)
    return len(pos_elem_set)

print(postional_elements([[1, 3, 4], [5, 2, 9], [8, 7, 6]]))

"""
rmin = 1,2,6
rmax = 4, 9, 8

colmin =  1, 2, 4
colmax = 8, 7, 9


1,1,1
1,1,1

1,1
1,1

"""