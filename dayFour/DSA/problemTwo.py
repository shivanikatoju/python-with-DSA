def sortedList(data, choice = True):
    sortedData = data
    if len(data) > 0:
        if choice is True:
            sortPos = 0
        else:
            sortPos = 1
        sortedData = sorted(data, key=lambda a: a[sortPos])
    return sortedData

def sortListCaller():
    myList = [(9, 'Hello'), (34, 'aaai'), (55, 'byeee'), (33, 'Bhaiii'), (65, 'Haiii')]
    print(f'myList: {myList}')
    newList = sortedList(myList)
    print(f'myList: {myList} --> {newList}')
    newList = sortedList(myList, False)
    print(f'myList: {myList} --> {newList}')

sortListCaller()