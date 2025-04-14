## Built-In Function
def string(x) :
  return x.reverse()



def reverse_string(s) :
  if len(s) == 0 :
      return ""
  return s[-1] + reverse_string(s[:-1])
  # return s[-1] + reverse_string(s[:len(s)-1])
