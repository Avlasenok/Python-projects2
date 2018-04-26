f = open("fuck", "r")
x = f.read()
x = x.splitlines()
print(repr(x))
print(x)
f.close()
print()

with open("/Users/avlasenok/Downloads/dataset_24465_4.txt", "r") as f, open("reversed.txt", "w") as target:
    x = f.read()
    x = x.splitlines()
    for i in (reversed(x)):
        target.write(i + "\n")

        #lines = open("input.txt").readlines()
        #with open("output.txt", "w") as out:
        #    out.writelines(reversed(lines))
        #Вот так было бы лаконично