def lucky_sum(a, b, c):
  s = 0
  list_of_n = [a,b,c]
  for e in list_of_n :
    if e != 13 :
      s += e
    else :
      break
  return s