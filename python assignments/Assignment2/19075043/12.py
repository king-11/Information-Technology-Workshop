def fun12(a: list):
    summation = 0
    for x in a:
        if type(x) == list:
            summation += sum(x)
        else:
            summation += x
    print(summation)

a = [1, 2, [3,4], [5,6]]
fun12(a)


    

        


