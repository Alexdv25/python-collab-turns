from utils import add_entry, read_entries

add_entry("Project initialized by A")
add_entry("B: first change")
add_entry("C: first change")

for line in read_entries():
    print(line)
