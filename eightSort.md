## 1 冒泡法
> 算法适用于少量数据的排序，时间复杂度为O(n^2)，是稳定的排序方法。需要进行的比较次数为第一轮 n-1，n-2....1, 总的比较次数为 n*(n-1)/2 
冒泡排序原理: 每一趟只能将一个数归位, 如果有n个数进行排序,只需将n-1个数归位, 也就是说要进行n-1趟操作(已经归位的数不用再比较)

![avatar](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1513837468750&di=80adbde9fea905f028d11eed783b8234&imgtype=0&src=http%3A%2F%2Fs4.51cto.com%2Fwyfs02%2FM00%2F7F%2F45%2FwKioL1cYja2QyroZAABJ7Vr_ICM404.png
)

```python   
    def bubble_sort(lists):
    # 冒泡排序
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists
    
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


![avatar](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1513855191642&di=a87d7df6af889b04aeb71ba957b0c147&imgtype=0&src=http%3A%2F%2Fimg0.ph.126.net%2FB-0Ay3zRizoehnnwSurEkw%3D%3D%2F1370220186727595322.jpg
)

```python
    
    def select_sort(lists):
    # 选择排序
    count = len(lists)
    for i in range(0, count):
        min = i
        for j in range(i + 1, count):
            if lists[min] > lists[j]:
                min = j
        lists[min], lists[i] = lists[i], lists[min]
    return lists
    
a = [1, 56, 2, 24, 5, 16, 8, 96, 45, 100, 1901, 89]
print selectsort(a)
[1, 2, 5, 8, 16, 24, 45, 56, 89, 96, 100, 1901]

```
### 3 插入排序

> 有一个已经有序的数据序列，要求在这个已经排好的数据序列中插入一个数，但要求插入后此数据序列仍然有序，这个时候就要用到一种新的排序方法——插入排序法,插入排序的基本操作就是将一个数据插入到已经排好序的有序数据中，从而得到一个新的、个数加一的有序数据，算法适用于少量数据的排序，时间复杂度为O(n^2)。是稳定的排序方法。插入算法把要排序的数组分成两部分：第一部分包含了这个数组的所有元素，但将最后一个元素除外（让数组多一个空间才有插入的位置），而第二部分就只包含这一个元素（即待插入元素）。在第一部分排序完成后，再将这个最后元素插入到已排好序的第一部分中。



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


### 4 希尔排序
> 希尔排序的实质就是分组插入排序，该方法又称缩小增量排序，
希尔排序，也称递减增量排序算法，是插入排序的一种更高效的改进版本。希尔排序是非稳定排序算法。
希尔排序是基于插入排序的以下两点性质而提出改进方法的：
插入排序在对几乎已经排好序的数据操作时，效率高，即可以达到线性排序的效率
但插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位

```python
#!/usr/bin/env python
# coding:utf-8

def shellSort(nums):
    # 设定步长
    step = len(nums)/2
    while step > 0:
        for i in range(step, len(nums)):
            # 类似插入排序, 当前值与指定步长之前的值比较, 符合条件则交换位置
            while i >= step and nums[i-step] > nums[i]:
                nums[i], nums[i-step] = nums[i-step], nums[i]
                i -= step
        step = step/2
    return nums
if __name__ == '__main__':
    nums = [9,3,5,8,2,7,1]
    print shellSort(nums)
```

### 5 归并排序
> 归并排序最令人兴奋的特点是：不论输入是什么样的，它对N个元素的序列排序所用时间与NlogN成正比。
基本思想：归并（Merge）排序法是将两个（或两个以上）有序表合并成一个新的有序表，即把待排序序列分为若干个子序列，每个子序列是有序的。然后再把有序子序列合并为整体有序序列。归并过程：比较a[i]和a[j]的大小，若a[i]≤a[j]，则将第一个有序表中的元素a[i]复制到r[k]中，并令i和k分别加上1；否则将第二个有序表中的元素a[j]复制到r[k]中，并令j和k分别加上1，如此循环下去，直到其中一个有序表取完，然后再将另一个有序表中剩余的元素复制到r中从下标k到下标t的单元。归并排序的算法我们通常用递归实现，先把待排序区间[s,t]以中点二分，接着把左边子区间排序，再把右边子区间排序，最后把左区间和右区间用一次归并操作合并成有序的区间[s,t]。



```python
def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        print 'i j ',i,j
        if left[i] <= right[j]:
            print 'left <right'
            print 'left[i],right[j] =',left[i],right[j]
            result.append(left[i])
            i += 1
        else:
            print 'left >right'
            print 'left[i],right[j] =',left[i],right[j]
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    num = len(lists) //2
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left, right)
a = [69,65,90,37,92,6,28,54,34]
print merge_sort(a)
```

![avatar](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1513835830465&di=6d3414e325591a72add55676c5aa5be4&imgtype=0&src=http%3A%2F%2Fimg.my.csdn.net%2Fuploads%2F201304%2F17%2F1366200577_4767.png
)



```python
/usr/bin/python /Users/zengfeng/PycharmProjects/algor_study/mergeSort.py
i j  0 0
left >right
left[i],right[j] = 69 65
i j  0 0
left >right
left[i],right[j] = 90 37
i j  0 0
left >right
left[i],right[j] = 65 37
i j  0 1
left <right
left[i],right[j] = 65 90
i j  1 1
left <right
left[i],right[j] = 69 90
i j  0 0
left >right
left[i],right[j] = 92 6
i j  0 0
left >right
left[i],right[j] = 54 34
i j  0 0
left <right
left[i],right[j] = 28 34
i j  0 0
left <right
left[i],right[j] = 6 28
i j  1 0
left >right
left[i],right[j] = 92 28
i j  1 1
left >right
left[i],right[j] = 92 34
i j  1 2
left >right
left[i],right[j] = 92 54
i j  0 0
left >right
left[i],right[j] = 37 6
i j  0 1
left >right
left[i],right[j] = 37 28
i j  0 2
left >right
left[i],right[j] = 37 34
i j  0 3
left <right
left[i],right[j] = 37 54
i j  1 3
left >right
left[i],right[j] = 65 54
i j  1 4
left <right
left[i],right[j] = 65 92
i j  2 4
left <right
left[i],right[j] = 69 92
i j  3 4
left <right
left[i],right[j] = 90 92
[6, 28, 34, 37, 54, 65, 69, 90, 92]

```
### 6 快速排序

> 快速排序基本思想是：通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。

![avatar](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1513839041454&di=e32f7740779f65cdd624b749df4f3896&imgtype=0&src=http%3A%2F%2Fimages2015.cnblogs.com%2Fblog%2F803394%2F201511%2F803394-20151130125447890-1717243395.jpg
)

```python
def quick_sort(lists, left, right):
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists
a = [1, 56, 2, 24, 5, 16, 8, 96, 45, 100, 1901, 89]
print quick_sort(a,0,len(a)-1)
[1, 2, 5, 8, 16, 24, 45, 56, 89, 96, 100, 1901]

```
