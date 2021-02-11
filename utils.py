import time

#print(time.ctime(1613057353.8781195))
#print(time.ctime(1613059256.3354304))

# Thu Feb 11 20:59:13 2021
# Thu Feb 11 21:30:56 2021
# Around 31 minutes for the inefficient way.

# part 2
import csv
import json
import time

print(time.ctime(time.time()))
list_dicts_difference = []

f1 = open('file1.json','r')
f2 = open('file2.json','r')

a = json.load(f1)
b = json.load(f2)

#set_list1 = set(tuple(sorted(d.items())) for d in a)
#set_list2 = set(tuple(sorted(d.items())) for d in b)

set_list1 = set()
set_list2 = set()
t1 = set()
t2 = set()

for d in a:
    items = d.items()
    t1.add(d['id'])
    set_list1.add(tuple(items))

for d in b:
    items = d.items()
    t2.add(d['id'])
    set_list2.add(tuple(items))


set_difference = set_list2.difference(set_list1)

# convert tuple to dict.
for element in set_difference:
    d = dict()
    for (x,y) in element:
        d[x] = y
    list_dicts_difference.append(d)
    
#for tuple_element in set_difference:
#     list_dicts_difference.append(dict((x, y) for x, y in tuple_element))


for i in list_dicts_difference:
    if(i['id'] == 2):
        print(i)

ausers = list()

busers = list()


""" for i in range(len(a)):
    ausers.append(a[i]['id'])
    
for i in range(len(b)):
    busers.append(b[i]['id'])

newElements = newElements(ausers,busers)

for element in a:
    if(element['id'] in newElements):
        list_dicts_difference.append(element)

for element in b:
    if(element['id'] in newElements):
        list_dicts_difference.append(element)

print(len(list_dicts_difference))
print(time.ctime(time.time())) """



print(len(list_dicts_difference))
# for i in range(len(a)):
#     ausers.append(a[i]['id'])    

# for i in range(len(b)):
#     busers.append(b[i]['id'])

# t1 = tuple(ausers)
# t2 = tuple(busers)

newElements = t1.symmetric_difference(t2)

print(len(newElements))

for element in a:
    if(element['id'] in newElements):
        list_dicts_difference.append(element)

for element in b:
    if(element['id'] in newElements):
        list_dicts_difference.append(element)

keys = ['id','phoneNumbers','locations','likes','newProperty']

with open('w2.csv','w',newline='') as output_file:
    writer = csv.DictWriter(output_file,keys)
    writer.writeheader()
    writer.writerows(list_dicts_difference)

print(len(list_dicts_difference))
print(time.ctime(time.time()))

