# -*- coding: utf-8 -*-
"""
Created on Thu May 21 15:41:21 2020

@author: LAVANYA
"""
import linecache
import time

from PyDictionary import PyDictionary

dictionary=PyDictionary()

start2=time.time()
f1=open(r"C:\Users\LAVANYA\Desktop\f5.txt",encoding="utf8")
word=input("enter the word to be searched:")
s=""
count=1
s=f1.readline()
l=s.split()
print(l)

while(s):
    s=f1.readline()
    l=s.split()
    if word in l:
        print("line number:",count,":",s)
    count+=1
end2=time.time()
print("searching completed in:",end2-start2,'milliseconds')

print("do you want to modify?y/n")
n=input()
if(n=='y'):
   
    linenumber=int(input("enter the line number to be modified:"))
    w=input("enter the word to be modified:")
    w1=input("enter the new word:")
    f=open(r"C:\Users\LAVANYA\Desktop\f5.txt","rt")
    data=f.read()
    data=data.replace(w,w1)
    f.close()
    f=open(r"C:\Users\LAVANYA\Desktop\f5.txt","wt")
    f.write(data) 
    f.close()
    print(linecache.getline(r"C:\Users\LAVANYA\Desktop\f5.txt",linenumber+1))   
    print("modified successfully!!!!")
else:
    ("end of modification")
print("do you want to see indexing?y/n")
q=input()
start1=time.time()
if(q=='y'):
    l=input("enter the word:")
    with open(r"C:\Users\LAVANYA\Desktop\f5.txt",encoding="utf8") as pack:
        with open(r"C:\Users\LAVANYA\Desktop\inde.txt","w") as index:
            count=0
            f=pack.read()
            s=f.replace("\n"," ")
            for line in s.split(" "):
                stri = line[:]
                index.write(stri+" ")
                c = str(count)
                index.write(c + "\n")
                count = len(line) + count
print("indexing completed")
end1=time.time()
print("indexing is done in:",end1-start1,"milliseconds")
print("do you want to annotate?y/n")
z=input()
if(z=='y'):
    ab=input("enter the word :")
    print(dictionary.meaning(ab))
else:
    print("end of annotation")
   
        