import csv
import json
import time

print(time.ctime(time.time()))

changedids = list()

# load the JSON files
f1 = open('file1.json','r')
f2 = open('file2.json','r')

a = json.load(f1)
b = json.load(f2)

# Initialize the sets() required for - to get the modified elements and new elments which are in file1 or file2
set_list1 = set()
set_list2 = set()
t1 = set()
t2 = set()

# Below code will find the difference between file2 and file1 elements

for d in a:
    items = d.items()
    t1.add(d['id'])
    set_list1.add(tuple(items))

for d in b:
    items = d.items()
    t2.add(d['id'])
    set_list2.add(tuple(items))

set_difference = set_list2.difference(set_list1)

# Converting the difference from tuple() ti dict()

for element in set_difference:
    d = dict()
    for (x,y) in element:
        d[x] = y
    changedids.append(d)
    
# find the symmetric_difference() to get the new elements and append those elements into global list

newElements = t1.symmetric_difference(t2)

for element in a:
    if(element['id'] in newElements):
        changedids.append(element)

for element in b:
    if(element['id'] in newElements):
        changedids.append(element)

# Convert the global list that got populated into CSV.

keys = ['id','phoneNumbers','locations','likes','newProperty']

with open('w2.csv','w',newline='') as output_file:
    writer = csv.DictWriter(output_file,keys)
    writer.writeheader()
    writer.writerows(changedids)

print(len(changedids))
print(time.ctime(time.time()))