import random
import json


phoneNumbers = ['3425145','143153','352432','34513535','3452421','2341564','3452352352','32465423446','3422623','355366','3425342']

locations = ['A','B','C','D','E','F','G','H','I','J','K']

likes = ["fJqwU","KBtDu","Qzata","QApeX","mwzFP","DQhGN","tkcdq","eNsaN","mbHtn","wZpEP","wZpEP","wZpEP"]

f1 = list()
for i in range(20002):
    r = random.randint(0,10)
    d = dict()
    d['id'] = i
    d['phoneNumbers'] = phoneNumbers[r]
    d['locations'] = locations[r]
    d['likes'] = likes[r]
    f1.append(d)

with open('file1.json', 'w') as file1:
    json.dump(f1,file1)
    
f2 = list()
for j in range(20002):
    if((j % 2) == 0):
        r = random.randint(0,10)
        d = dict()
        d['id'] = j
        d['phoneNumbers'] = phoneNumbers[r]
        d['locations'] = locations[r]
        d['likes'] = likes[r]
        f2.append(d)
    elif((j % 7) == 0):
        r = random.randint(0,10)
        d = dict()
        d['id'] = j
        d['phoneNumbers'] = phoneNumbers[r]
        d['locations'] = locations[r]
        d['likes'] = likes[r]
        d['newProperty'] = str(r)
        f2.append(d)
        
    

with open('file2.json', 'w') as file2:
    json.dump(f2,file2)