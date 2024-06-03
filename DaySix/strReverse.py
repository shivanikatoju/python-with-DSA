def myStrRevOne(myStr):
    myList = [*myStr]
    myList.reverse()
    return ''.join(myList)
 
def myStrRevTwo(myStr):
    return myStr[::-1]
 
def myStrRevThree(myStr):
    str3 = [*myStr]
    strLen = len(myStr)
    for i in range(strLen//2):
        str3[i], str3[strLen-i-1] = str3[strLen-i-1],str3[i]
    return ''.join(str3)
 
if __name__ == '__main__':
    mystr1 = 'Hello'
    mystr2 = 'World'
    mystr3 = 'pots & pans'
 
    res = myStrRevOne(mystr1)
    print(f'Rev: {mystr1} --> {res}')
 
    res = myStrRevTwo(mystr2)
    print(f'Rev: {mystr2} --> {res}')
 
    res = myStrRevThree(mystr3)
    print(f'Rev: {mystr3} --> {res}')

