def callme(r):
  if r == "":
    return r
  else: 
    return callme(r[1:]) + r[0]

example = "Hello World"
print(callme(example))