import csv
import json
import time

f1 = open('file1.json','r')
f2 = open('file2.json','r')

a = json.load(f1)
b = json.load(f2)

changedids = list()
ausers = list()
busers = list()

# Function that will return the elements which only in file1 or file2
def newElements(a,b):
    d = list()
    for i in a+b:
        if(i not in a or i not in b):
            d.append(i)
    return d

# Below code will add all the unique ids in the lists created above
for i in range(len(a)):
    ausers.append(a[i]['id'])
    
for i in range(len(b)):
    busers.append(b[i]['id'])
    
# Below code will give a list that will have only modified elements w.r.t file2

for i in range(len(a)):
    temp1 = a[i].items()
    for j in range(len(b)):
        if(b[j]['id'] == a[i]['id']):
            temp2 = b[j].items()
            if(not temp2 == temp1):
                updates = dict()
                updates['id'] = b[j]['id']              
                diff = set(temp2).difference(temp1)
                for (e,v) in diff:
                    updates[e] = v
                changedids.append(updates)

# Below code will add all the elements that either in file1 or in file2

newElements = newElements(ausers,busers)
for element in a:
    if(element['id'] in newElements):
        changedids.append(element)

for element in b:
    if(element['id'] in newElements):
        changedids.append(element)

# Below code will write the list into CSV file.

keys = ['id','phoneNumbers','locations','likes','newProperty']

with open('w.csv','w',newline='') as output_file:
    writer = csv.DictWriter(output_file,keys)
    writer.writeheader()
    writer.writerows(changedids)

print(time.ctime(time.time()))