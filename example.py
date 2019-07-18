import random
import pyid


mylist = [random.sample(range(10), k=3) for i in range(20)]


# Use python uuid module to assign ID by default
mylist = [pyid.idfy(item) for item in mylist]
for item in mylist:
    print(item, item.id)


# Assign a custom ID
mylist = [pyid.idfy(item, 'myid') for item in mylist]
for item in mylist:
    print(item, item.id)
