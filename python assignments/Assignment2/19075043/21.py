from random import randrange
from datetime import timedelta
from datetime import datetime

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

x,y = input("Enter dates ").split()

date1 = datetime.strptime(x,'%m/%d/%Y')
date2 = datetime.strptime(y,'%m/%d/%Y')

rand = random_date(date1,date2).date()

print(str(rand.month)+"/"+str(rand.day)+"/"+str(rand.year))