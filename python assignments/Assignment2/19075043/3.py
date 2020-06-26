def func3(*nums):
    for x in nums:
        y = {'subject':x['subject'],'id':x['id']}
        classes = []
        sum = 0 
        count = 0
        for z in x:
            if z != 'subject' and z != 'id':
                classes.append(z)
                sum += x[z]
                count += 1
        y["+".join(classes)] = sum/count
        print(y)
        

func3({'id' : 1, 'subject' : 'math', 'V' : 70, 'VI': 82},
{'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
{'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86})

    