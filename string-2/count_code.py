def count_code(str):
  c = 0
  for i in range(len(str)-3) :
    e = str[i:i+4]
    if e[0] == "c" and e[1] == "o" and e[3] == "e" :
      c += 1
  return c