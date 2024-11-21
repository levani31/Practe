#### convert from dictionary to json => json.dumps(variable)
import json
# dic = {
#     "name":"Levani",
#     "lastName":"Mtchedlishvili",
#     "isEmployed":False
# }
# print(json.dumps(dic))
#
# ### convert from json to dictionary => json.loads(variable)
# jsonVar = json.dumps(dic)
# print(json.loads(jsonVar))
#
#
# ### convert from json file to dictionary
# with open("data.json",) as data:
#     print(json.load(data))

data2 = {"age":22}
with open("data.json","w") as file:
    file.write(json.dumps(data2))
    print(json.load(file))
