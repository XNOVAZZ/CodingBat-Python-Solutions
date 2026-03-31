def make_bricks(small, big, goal):
  if big*5 > goal :
    if goal % 5 <= small :
      return True
    else :
      return False
  else :
    if goal - big*5 <= small :
      return True
    else :
      return False