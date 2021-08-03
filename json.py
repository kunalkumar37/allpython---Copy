#json is a syntax for storing and exchanging data

#json text written in javascript

"""" if you have a json string, you can parse it by using json.loads() method
"""

#json has a built in package called json which can be used ot work with json data
"""import json
# some json
x =  '{ "name":"John", "age":30, "city":"New York"}'

#parse x
y=json.loads(x)

print(y["age"])"""

import json

x={"name": "John",
  "age": 30,
  "city": "New York"
  }

y=json.dumps(x)
print(y)