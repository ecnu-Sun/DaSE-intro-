#第一题 第二题 程序执行时间只要用结束时间减去初始时间
import time
def is_prime(a):
    if(a==1):
        return 0
    if(a==2):
        return 1
    i=2
    while (i*i< a or i*i==a):
        if(a%i==0):
            return 0
        i=i+1
    return 1

a=int(input("a="))
st=time.time()
print(is_prime(a))
ed=time.time()
print("运行时间"+str(ed-st))

#第三题
def insert_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

li=[1,5,7,3,2,6]
print(insert_sort(li))

#第四题
#希尔排序最坏时间复杂度是O（n^2) （数组逆序，并且间隔每次缩小一半）最好时间复杂度是O（n） （数组已经排好序时）
#空间复杂度是O（1）
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap //= 2

    return arr

arr = [12, 34, 54, 2, 3]
print(shell_sort(arr))  
