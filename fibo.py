## 迭代的方式，这个方式比递归的更有效
def fibo(num):
    numList = [0,1]

    for i in range(num - 2):
        numList.append(numList[-2] + numList[-1])
    return numList
