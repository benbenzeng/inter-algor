## 1 冒泡法
* 算法适用于少量数据的排序，时间复杂度为O(n^2)，是稳定的排序方法。需要进行的比较次数为第一轮 n-1，n-2....1, 总的比较次数为 n*(n-1)/2

> 比如有五个数: 12, 35, 99, 18, 76, 从大到小排序, 对相邻的两位进行比较

- 第一趟:

> 第一次比较: 35, 12, 99, 18, 76

> 第二次比较: 35, 99, 12, 18, 76

> 第三次比较: 35, 99, 18, 12, 76

> 第四次比较: 35, 99, 18, 76, 12

> 经过第一趟比较后, 五个数中最小的数已经在最后面了, 接下来只比较前四个数, 依次类推

- 第二趟
> 99, 35, 76, 18, 12
> 第三趟
> 99, 76, 35, 18, 12
> 第四趟
> 99, 76, 35, 18, 12
> 比较完成
* 冒泡排序原理: 每一趟只能将一个数归位, 如果有n个数进行排序,只需将n-1个数归位, 也就是说要进行n-1趟操作(已经归位的数不用再比较)

```python
def bubbleSort(nums):
 #一共进行几轮列表比较,一共是(length-1)轮
    for i in range(0，len(nums)-1):
 #每一轮的比较,注意range的变化,这里需要进行length-1-长的比较,注意-i的意义(可以减少比较已经排好序的元素)   
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums
  #交换
12             if myList[j] > myList[j+1]:
13                 tmp = myList[j]
14                 myList[j]=myList[j+1]
15                 myList[j+1] = tmp

nums = [5,2,45,6,8,2,1,100,1901,9]
```

## 2 直接选择排序
> 基本思想：选出最小的一个和第一个位置交换，选出其次小的和第二个位置交换 ……
直到从第N个和第N-1个元素中选出最小的放在第N-1个位置。
选择排序的复杂度分析。第一次内循环比较N - 1次，然后是N-2次，N-3次，……，最后一次内循环比较1次。
共比较的次数是 (N - 1) + (N - 2) + ... + 1，求等差数列和，得 (N - 1 + 1)* N / 2 = N^2 / 2。
舍去最高项系数，其时间复杂度为 O(N^2)。
虽然选择排序和冒泡排序的时间复杂度一样，但实际上，选择排序进行的交换操作很少，最多会发生 N - 1次交换。
而冒泡排序最坏的情况下要发生N^2 /2交换操作。从这个意义上讲，交换排序的性能略优于冒泡排序。
而且，交换排序比冒泡排序的思想更加直观。

```python
def selectsort(lists):
    lenlistst = len(lists)
    for i in range(lenlistst):
        for j in range(i+1,lenlistst):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists
a = [1, 56, 2, 24, 5, 16, 8, 96, 45, 100, 1901, 89]
print selectsort(a)
[1, 2, 5, 8, 16, 24, 45, 56, 89, 96, 100, 1901]

```
3 插入排序

> 有一个已经有序的数据序列，要求在这个已经排好的数据序列中插入一个数，但要求插入后此数据序列仍然有序，这个时候就要用到一种新的排序方法——插入排序法,插入排序的基本操作就是将一个数据插入到已经排好序的有序数据中，从而得到一个新的、个数加一的有序数据，算法适用于少量数据的排序，时间复杂度为O(n^2)。是稳定的排序方法。插入算法把要排序的数组分成两部分：第一部分包含了这个数组的所有元素，但将最后一个元素除外（让数组多一个空间才有插入的位置），而第二部分就只包含这一个元素（即待插入元素）。在第一部分排序完成后，再将这个最后元素插入到已排好序的第一部分中。
<img src="https://gss1.bdstatic.com/9vo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike72%2C5%2C5%2C72%2C24/sign=5e4a531a252dd42a4b0409f9625230d0/d0c8a786c9177f3eee69fa7e70cf3bc79f3d5667.jpg
" width="200px" />


![avatar](https://gss1.bdstatic.com/9vo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike72%2C5%2C5%2C72%2C24/sign=5e4a531a252dd42a4b0409f9625230d0/d0c8a786c9177f3eee69fa7e70cf3bc79f3d5667.jpg
)


```python
def insertSort(lists):
    for i in range(1,len(lists)):
        if lists[i-1]>lists[i]:
            index = i # 当前需要排序的元素
            temp = lists[i] # 用来记录排序元素需要插入的位置
            while index>0 and lists[index-1]>temp:
                lists[index]= lists[index-1] # 腾出位置，把已经排序好的元素后移一位，留下需要插入的位
                index = index-1
            lists[index]=temp # 把需要排序的元素，插入到指定位置
    return lists

a = [1, 56, 2, 24, 5, 16, 8, 96, 45, 100, 1901, 89]
print insertSort(a)
[1, 2, 5, 8, 16, 24, 45, 56, 89, 96, 100, 1901]

```
