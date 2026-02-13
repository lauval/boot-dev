stuff = [1,2,3,4,5]


for element in stuff:
    to_keep = stuff.copy()
    to_keep.remove(element)
    print(to_keep)