def parrot_trouble(talking, hour):
  trouble = False
  if talking is True and ( hour < 7 or hour > 20) :
    trouble = True 
  return trouble