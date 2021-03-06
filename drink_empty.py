“’今天面试问到一个算法: 一个汽水是$1, 两个汽水的空瓶换一瓶可乐, 请问给一些钱, 最多能喝几瓶呢? 
当时思路有些乱, 算法没写清楚, 面试结束去个奶茶店, 重新写了一下.


英文的描述:
A bottle of Coke is $1. You can exchange two empty bottles for a bottle of Coke. You have $20 now in your pocket. 
So how many bottles of Coke can you drink at most?“’

# 方法1 当时写算法的时候, 面试官很看重的是可读性, 例如变量名的定义. 
# 作为一个Python程序员, 我以后也在这方面也要更加注意.

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
