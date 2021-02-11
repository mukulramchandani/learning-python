import csv
import json
import time



f1 = open('file1.json','r')
f2 = open('file2.json','r')

a = json.load(f1)
b = json.load(f2)

# #print(type(a[0]))

# for i in range(0, len(a)):
#     dict1 = a[i]
#     dict2 = b[i]
#     set1 = set(dict1.items())
#     set2 = set(dict2.items())
#     diff = set1.difference(set2)
#     print(diff)

# print(0 == 0.0)

# #print(set(a[0].items()))

# # for n in "banana":
# #     print(n)

# word = "banananana"
# i = word.find("na", 1)
# print(i)

# d = dict()
# print(d.get('a', 0))

# # Count the number of words in a file
# handle = open('text.txt', 'r')
# counts = dict()

# for line in handle:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
# print(counts)

# bigcount = None
# bigword = None
# for word, count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count

# print(bigword, bigcount)
# print(counts.items())

print('--------------\n-----------\n----')
print(time.ctime(time.time()))
changedids = list()
ausers = list()
busers = list()


def newElements(a,b):
    d = list()
    for i in a+b:
        if(i not in a or i not in b):
            d.append(i)
    return d


for i in range(len(a)):
    ausers.append(a[i]['id'])
    
for i in range(len(b)):
    busers.append(b[i]['id'])

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



newElements = newElements(ausers,busers)
for element in a:
    if(element['id'] in newElements):
        changedids.append(element)

for element in b:
    if(element['id'] in newElements):
        changedids.append(element)

#print(changedids)

keys = ['id','phoneNumbers','locations','likes','newProperty']

with open('w.csv','w',newline='') as output_file:
    writer = csv.DictWriter(output_file,keys)
    writer.writeheader()
    writer.writerows(changedids)

print(time.ctime(time.time()))






