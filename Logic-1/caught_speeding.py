def caught_speeding(speed, is_birthday):
  if is_birthday == True :
    if speed <= 65 :
      return 0
    elif speed > 85 :
      return 2
    else :
      return 1
  else :
    if speed <= 60 :
      return 0
    elif speed > 80 :
      return 2
    else :
      return 1