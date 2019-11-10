## 1. What is the output of the following?¶
    x = ['ab', 'cd']
    for i in x:
        i.upper()
    print(x)

## 2. What is the output of the following?¶
    x = ['ab', 'cd']
    for i in x:
        x.append(i.upper())
    print(x)

## 3. What is the output of the following?¶
    x = "abcdef"
    i = "a"
    while i in x:
        x = x[:-1]
        print(i, end = " ")

## 5. What is the output of the following?¶
    names = ['Amir', 'Bear', 'Charlton', 'Daman']
    print(names[-1][-1])