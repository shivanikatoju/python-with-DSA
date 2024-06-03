from random import randint

def mySort(dataList):
    for i in range(len(dataList)):
        for j in range(i + 1, len(dataList)):
            if dataList[i] > dataList[j]:
                dataList[j], dataList[i] = dataList[i], dataList[j]

    return dataList

lst = []
for i in range(10):
    t = randint(1,100)
    lst.append(t)
print(mySort(lst))