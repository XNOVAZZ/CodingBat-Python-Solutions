def string_match(a, b):
  c = 0
  l = min(len(a),len(b)) #find shorter
  for i in range(l-1) :
    if a[i:i+2] == b[i:i+2] :
          c += 1
  return c
  


