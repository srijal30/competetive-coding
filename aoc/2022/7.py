testerfile = open('7', 'r')
content = testerfile.read()
testerfile.close()
lines = content.splitlines()

dirs = {}

class Node:
    def __init__(self, path, parent):
        self.path = path
        self.parent = parent
        self.files = {}
        self.dirs = {}

    def size(self):
        return sum(list(self.files.values()))

    def take_file(self, name, size):
        self.files[name] = size
        if self.parent:
            self.parent.take_file(name, size)

current_dir = Node("/", None)
dirs["/"] = 0

total_size = 0
for line in lines:
    if line[0:7] == "$ cd /":
        current_dir = dirs["/"]
    elif line[0:8] == "$ cd ..":
        current_dir = current_dir.parent
    elif line[0:4] == "$ cd":
        current_dir = Node(current_dir.path + line[5::] + "/", current_dir)
        dirs[current_dir.path] = 0
    elif "$ ls" in line:
        pass
    elif "dir " in line:
        pass
    else:
        size, name = line.split(" ")
        size = int(size)
        current_dir.take_file(name, size)

        tmp_path = current_dir.path
        while tmp_path != "":
            dirs[tmp_path] += size
            tmp_path = tmp_path[0:tmp_path.rfind("/")]
            tmp_path = tmp_path[0:tmp_path.rfind("/")+1]
        dirs["/"] += size
        total_size += size



req = 30000000 - (70000000 - total_size)

sizes  = [dir for dir in list(dirs.values())]
#sizes  = [dir.size() for dir in list(dirs.values())]
sizes.sort()
print(sizes)
for x in sizes:
    if x >= req:
        print(x)
        break
