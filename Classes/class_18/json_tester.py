import json

me = {
    'name':'Eyal',
    'age':5,
    'city':"New York"
}

myfile = open("database.json", "w")
json.dump(me, myfile)
myfile.close()

### READING THE DATABASE

myfile = open("database.json", 'r')

content = json.load(myfile)

print(content)

myfile.close()





