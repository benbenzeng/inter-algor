input: 
1. 给定一个升序排列的自然数数组, eg. [1, 3, 3, 5, 7, 7, 7, 7, 8, 14, 14] 
2. 任意自然数, eg. 7 
output: 
数组内 值为7区域的左右边界index: [1, 3, 3, 5, 7, 7, 7, 7, 8, 14, 14] 
这个例子中就是(4, 7)
1 方法1 我自己的，没有用到二叉树
def search(num_list, num):
    section = []
    for i in range(len(num_list)):
        if num_list[i]==num:
            section.append(i)
    return min(section),max(section)

a = [1, 3, 3, 5, 7, 7, 7, 7, 8, 14, 14] 
print search(a, 7)
output： 4 7
2 方法2 
https://changchen.me/blog/20170306/binary-search/   没有看懂
