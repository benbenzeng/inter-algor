#!/usr/bin/env python
def search2(a,m):
    low = 0
    high = len(a) - 1
    while(low <= high):
        mid = (low + high)/2
        midval = a[mid]

        if midval < m:
            low = mid + 1
        elif midval > m:
            high = mid - 1
        else:
            print mid
            return mid
    #print -1
    #return -1

if __name__ == "__main__":
    a = [10,11,12,16,18,23,29,33,48,54,57,68,84,98]
    m = 54
    search2(a,m)
