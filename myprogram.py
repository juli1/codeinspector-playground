import logging

def myfunction(arg, arg2):
  """
  add two numbers
  :arg: the first parameter
  :arg2: the second parameter
  """
  res = arg + arg2
  print("returning {0}".format(res))
  return res

myfunction(1, 2)
