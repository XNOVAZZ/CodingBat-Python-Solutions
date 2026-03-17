def centered_average(nums):
  nums.sort()
  centered = nums[1:-1]
  avg = sum(centered) // len(centered)
  return avg
