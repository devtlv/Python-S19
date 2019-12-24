import os

files = os.scandir('../class_17')

word2search = "json"

os.path.join

for f in files:
    if not os.path.isfile(f):
        continue
    filepath = f.path
    content = open(filepath, 'r').read()
    if word2search in content:
        print("=======",f.name)
        print(content)
        print('\n')
