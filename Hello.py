data=[111111111,'dtkcauycvelauycal',3.3333]
i=0
while i<len(data):
    if isinstance(data[i] ,float):
        data[i]=data[i] % 1


i=i+1
print(data[i])

