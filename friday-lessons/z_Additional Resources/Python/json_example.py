import json

# read JSON file in
my_array = json.loads(open("example.json", "r").read())

# print basic info about the object
print("There are "+str(len(my_array))+" logs in this JSON file")
print("There are",len(my_array[0].keys()),"keys in each log, and the keys are:")
print(my_array[0].keys())

# print _type of each log
print("\n\nIDs of logs:")
for log in my_array:
    print(log["_id"])