#Bruk Thomas Tewelde
#PSID: 1834503
parts = input().split()
name = parts[0]

while name != '-1':
    try:
        age = int(parts[1]) + 1

        # outputs name & age
        print('{} {}'.format(name, age))

    except ValueError:

        # prints the name and specified age with 0
        print('{} {}'.format(name, 0))

    parts = input().split()
    name = parts[0]