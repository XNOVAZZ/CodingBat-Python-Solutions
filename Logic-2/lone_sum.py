def lone_sum(a, b, c):
  s = a + b + c
  if a == b == c :
    return 0
  elif a == b :
    return s - a - b
  elif a == c :
    return s - a - c
  elif b == c :
    return s - b - c
  else :
    return s
