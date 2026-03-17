def has22(nums):
  has_22 = False
  for i in range(len(nums)-1) :
    if nums[i] == 2  :
      if nums[i+1] == 2 :
        has_22 = True
  return has_22
