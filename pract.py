import json

a = 10
b = 20
c = a + b
print(c)

if c < 60:
    name = "cool"
    date = "ramu"
    ri = name+date
    sal = "Country: India"

else:
    print("Jai Hind")

print(name+date)
#JSON code
# {key:value mapping} 
a ={"name":ri, 
   "age":c, 
    "Salary":sal} 
  
# conversion to JSON done by dumps() function
b = json.dumps(a) 
  
# printing the output 
print(b)

with open('demo.json', 'w') as json_file:  
    json.dump(a, json_file)
