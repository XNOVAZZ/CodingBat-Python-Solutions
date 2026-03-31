def round10(num) :
  if num % 10 >= 5 :
    return ((num // 10) + 1) * 10
  else :
    return ((num // 10) ) * 10
def round_sum(a, b, c):
  s = 0
  list_num = [a,b,c]
  for e in list_num :
    s += round10(e)
  return s
