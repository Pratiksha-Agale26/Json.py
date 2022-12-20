import json
d={"pratiksha":1,"Agale":2}
file=open("my_name.json","w")
b=json.dump(d,file)
# mystring=json.dumps(a)

print(d)