def func9(*sets):
    union = list()
    intersect = sets[0]
    for x in sets:
        union = list(set(union)|set(x))
        intersect = list(set(intersect) & set(x))
    
    diff = []
    for x in range(len(sets)):
        diff.append([])
        for y in sets[x]:
            if y not in intersect:
                diff[x].append(y)

    print("Union is",union,"\nIntersection is",intersect,"\nDifference is",diff)

        

func9(["green", "blue"],["blue", "yellow"])
