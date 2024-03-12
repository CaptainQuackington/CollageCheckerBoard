rows = int(input("How many rows does the checker board have"))
columns = int(input("How many columns does the checker board have"))

pattern1 = input("What is the first pattern")
pattern2 = input("What is the second pattern")

for i in range(rows):
    switch = "a"
    table = []
    for j in range(columns):
        if switch == "a":
            table.insert(j, pattern1)
            switch = "b"
        elif switch == "b":
            table.insert(j,pattern2)
            switch = "a"
    print(table)
