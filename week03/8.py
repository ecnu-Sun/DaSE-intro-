import random
import time

def random_list(len):
    return [random.randint(1, 100) for _ in range(len)]

def select_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

lists=[]
for i in range(0,100):
    lists.append(random_list(random.randint(100,200)))
s=time.time()
for i in range(0,100):
    select_sort(lists[i])
e=time.time()
print(e-s)

lists2=[]
for i in range(0,100):
    lists2.append(random_list(random.randint(100,200)))
s2=time.time()
for i in range(0,100):
    select_sort(lists2[i])
e2=time.time()
print(e2-s2)
