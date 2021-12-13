# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 00:23:28 2021

@author: botanky
"""

from operator import itemgetter #Sıklık listesi için
from time import process_time
start = process_time()
with open('test.txt', encoding="utf8") as file:
    lines = file.read()
lines = lines.splitlines()
for x in range(len(lines)):
    lines[x] = lines[x].split(" ")
file.close()
wordlist = []
unique = dict()
c=0
collocation = []

punc = '''!()-[]{};:'"\, <>./?@#$^&*_~%0123456789'''
#Kelime başında ve sonundaki noktalama işaretlerini kaldırıp kelime içindeki noktalama işaretlerini bıraktım.
while 1:
    N = int(input("type length of the collocation(for example 2 for two-word collocations) = "))
#    if N == 2 or N == 3:
    break
#    else:
#        print("Type 2 or 3")

for y in range(len(lines)):
    for z in range(len(lines[y])):
        wordlist.append(lines[y][z])
for i in range(len(wordlist)):
    row=[]
    for a in range(1):
        row.append(0)
    collocation.append(row)

for x in range(len(wordlist)):
    if wordlist[x][0] in punc:
        c += 1
        collocation[c].append(wordlist[x])
        if wordlist[x][-1] in punc:
            c += 1
    elif wordlist[x][-1] in punc:
        collocation[c].append(wordlist[x])
        c += 1
    else:
        collocation[c].append(wordlist[x])
        continue

for x in range(len(collocation)):
    collocation[x].pop(0)
x=0
while x < len(collocation):
    if len(collocation[x])<N:
        collocation.pop(x)
        x -= 1
    x += 1

coll = []
for x in range(len(collocation)):
    for y in range(len(collocation[x])-(N-1)):
        coll.append(collocation[x][y])
        for z in range(1,N,1):
            coll[len(coll)-1] = coll[len(coll)-1]+" "+collocation[x][y+z]
occurance = dict()
for y in range(len(coll)):
    if coll[y] in occurance:
        occurance[coll[y]]+=1
        break
    else:
        occurance[coll[y]]=1
occurance = sorted(occurance.items(), key = itemgetter(1), reverse = True)

print("\n-THE MOST FOUND COLLOCATIONS-")
for x in range(0,3,1):
    print("{0}: {1}".format(occurance[x][0],occurance[x][1]))
    
stop = process_time()
print(stop-start)

        
    