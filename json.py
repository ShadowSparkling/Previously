import json
#Fist IMPORT JSON module fro json stuffs
# JSON to PY use loads()
#PY to JSON use dumps()

#some JSON
x = '{"name":"Sayak", "age":47747, "job":"Programmer"}'

#parse JSON
y = json.loads(x)
print(y["age"])

print(x)


a = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

b = json.dumps(a)
print(b)
