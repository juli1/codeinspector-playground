import logging

def func(arg):
  print("super arg {0}".format(arg))
  print("super arg {0}".format(arg))

def func2(arg):
  print("super arg {0}".format(arg))

def func3(arg):
  logging.info("super arg {0}".format(arg))

func("bla")
func2("bla")
func3("bla")


