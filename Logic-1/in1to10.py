def in1to10(n, outside_mode):
  if outside_mode == True :
    if n >= 10 :
      return True
    elif n <= 1 :
      return True
    else :
      return False
  else :
    if 1 <= n <= 10 :
      return True
    else :
      return False
      
    
