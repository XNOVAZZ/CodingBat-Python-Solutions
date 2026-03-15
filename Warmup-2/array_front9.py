def array_front9(nums):
  c = 1
  a = False #a obtain boolean
  for i in range(len(nums)) :
    if c <= 4 :
      if nums[i] == 9 :
          a = True
    c += 1
  return a
    
