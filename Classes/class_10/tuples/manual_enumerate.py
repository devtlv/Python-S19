names = ['Rick', 'Morty', 'Beth', 'Jerry', 'Summer']

# 1st method
index = 0

for name in names:
    print(name,'--', index)
    index += 1

print('-'*30)

# 2nd method
index = 0
while index < len(names):
    print('{} -- {}'.format(names[index], index))
    index += 1

print('-'*30)

# 3rd method
for index in range(len(names)):
    print('{} -- {}'.format(names[index], index))

# Rick -- 0
# Morty -- 1
# Beth -- 2
# Jerry -- 3
# Summer -- 4

