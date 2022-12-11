testerfile = open('6', 'r')
content = testerfile.read()
testerfile.close()
lines = content.splitlines()

for index in range(len(content)):
    if index < len(content)-14:
        if len(set(content[index:index+14])) == 14:
            print(content[index:index+14])
            print(index+14)
            break

