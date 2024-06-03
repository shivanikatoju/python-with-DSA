def isPrime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def countMaxZeroes(lst):
    count = 0
    max_count = 0
    for i in range(len(lst)-1):
        if lst[i] == 0:
            count+=1
        else:
            s = lst[i]
            if count > max_count:
                max_count = count
            count = 0
    if count > max_count:
        max_count = count
    print('start',s)

    return max_count

if __name__ == '__main__':
    start = int(input("Enter the start value: "))
    lst = [_ for _ in range(start, start+100)]
    print(lst)
    for i in range(len(lst)):
        if not isPrime(lst[i]):
            lst[i] = 0
    print(lst)
    print(f'The number of zeroes between {start} and {start+100} are/is:', countMaxZeroes(lst))