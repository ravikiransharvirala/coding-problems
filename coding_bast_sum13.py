def sum13(nums):
  if not nums:
    return 0
  else:
    sum_nums = 0
    for i in range(len(nums)):
      if nums[i] != 13 and nums[i-1] != 13:
        sum_nums += nums[i]
  return sum_nums


nums = [1, 2, 2, 1, 13]

print(sum13(nums))