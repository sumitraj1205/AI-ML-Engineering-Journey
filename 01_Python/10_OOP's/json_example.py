import json
json_str = '{"sumit" : "boy","college" : "hit","is_male" : true}'
json_py = json.loads(json_str)
print(type(json_py),json_py,type(json_str))
a = {
    "sumit" : "boy",
    "college" : "hit",
    "is_male" : True,
    "adress" : {
        "state" : "jh",
        "pin" : 826001
    }
}
b = json.dumps(a)
print(type(b),b,type(a))
with open("samplee.json","r") as f:
    print(f.read())
