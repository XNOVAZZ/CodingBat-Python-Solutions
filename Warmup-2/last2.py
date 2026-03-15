def last2(str):
  last2 = str [-2:]
  r_str = str[:-1] #r is remain
  c = 0
  for i in range(len(r_str)-1) :
    if r_str[i:i+2] == last2 :
      c += 1
  return c
    
    
