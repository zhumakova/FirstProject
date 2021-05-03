# with open('text.txt','r') as file1:
#     print(file1.read())

import sys

countdown=int(sys.argv[1])
astronaut_name=sys.argv[2]
for i in range(1,countdown+1):
    print(i)
    if i==countdown:
        print('Go!-',astronaut_name)