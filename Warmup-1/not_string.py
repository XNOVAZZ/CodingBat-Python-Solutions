def not_string(str):
    if len(str) >= 3 :
      if str[:3] != "not" :
        str = "not"+" "+str
        return str
      else :
        return str
    else :
      str = "not"+" "+ str
      return str
  