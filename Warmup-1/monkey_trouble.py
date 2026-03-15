def monkey_trouble(a_smile, b_smile):
  WAIT = False # WAIT stand for we are in Trouble
  if (a_smile is True and b_smile is True) or (a_smile is False and b_smile is False) :
    WAIT = True
  return WAIT
