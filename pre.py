import json

file = open("data.txt","r")

data = file.readlines()

for i in data:
    d = json.loads(i)
    print('("%s","%s",%d,%d,%d)'%(d["entry_time"],d["exit_time"],0,d["entry_gate"],d["exit_gate"]))