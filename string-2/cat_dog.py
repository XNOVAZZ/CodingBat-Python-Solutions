def cat_dog(str):
  cat_c = 0
  dog_c = 0
  for i in range(len(str)-2) :
    if str[i:i+3] == "cat" :
      cat_c += 1
    elif str[i:i+3] == "dog" :
      dog_c += 1
      
  return (cat_c == dog_c)
