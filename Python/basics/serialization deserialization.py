
import json

# JSON string
students = '{"id":"9607", "name": "Sunny", "department":"Computer"}'
# deserialization
studentdict = json.loads(students)
print(studentdict['name'])

data = {
    "id": "877",
    "name": "Mayur",
    "department": "Comp"
}

# serialization
studentStr = json.dumps(data)
print(studentStr)

import pickle
with open('data.pickle', 'wb') as f1:
    # converts object to byte stream(list, dict, etc.)
    # serialization
    pickle.dump(students, f1)
    print("Pickling completed")

with open('data.pickle', 'rb') as f2:
    # desrialization
    data = pickle.load(f2)
    print(data)
