# 方法1 当时写算法的时候, 面试官很看重的是可读性, 例如变量名的定义. 
作为一个Python程序员, 我以后也在这方面也要更加注意.

def cal_drinks(n):
    avail_drinks = n
    sum_drunk = 0
    empty_drinks = 0

    while avail_drinks > 0:
        # consume available drinks
        sum_drunk += avail_drinks
        empty_drinks += avail_drinks

        # replace empty bottles to drinks
        avail_drinks = empty_drinks // 2
        empty_drinks = empty_drinks % 2

    return sum_drunk



# 方法2 递归方法：最重要的两个公式
##  n个空瓶: f(n) = n/2 + f(n/2 + n%2)
##  n块钱:  F(n) = n + f(n)
def cal_drinks_by_empty(n):
    if n <= 1:
        sum_drunk = 0
    else:
        sum_drunk = n//2 + cal_drinks_by_empty(n//2 + n%2)

    return sum_drunk


def cal_drinks(n):
    return n + cal_drinks_by_empty(n)
print cal_drinks(20)   #输出 39

## 除法运算// 返回商的整数部分，抛弃余数
divisorNumber=10//3
print(divisorNumber)        #输出结果：3
