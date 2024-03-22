import numpy as np
from random import randrange
import sys

def insertion_sort(data,gap):
    for i in range(gap,len(data)):
        current = data[i]
        j = i 
        while current < data[j-gap] and j>=gap:
            data[j] = data[j-gap]
            j -= gap
        data[j] = current
    return data

def selection_sort(data):
    n = len(data)
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if data[j] < data[min]:
                min = j
        data[i], data[min] = data[min], data[i]
    return data

def partition(data, low, high):
    pivot = data[low]
    greater = high
    for i in range(high,low,-1):
        if data[i] > pivot:
            data[greater], data[i] = data[i], data[greater]
            greater-=1
    data[low], data[greater] = data[greater], data[low]
    return greater


def quick_sort_left(data,low,high):
    if low < high:
        i = partition(data,low,high)
        quick_sort_left(data,low,i-1)
        quick_sort_left(data,i+1,high)
    return data

def iterative_quicksort(arr):
    if len(arr) <= 1:
        return arr

    stack = [(0, len(arr) - 1)]
    
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(arr, low, high)
            if pivot_index - low < high - pivot_index:
                stack.append((pivot_index + 1, high))
                stack.append((low, pivot_index - 1))
            else:
                stack.append((low, pivot_index - 1))
                stack.append((pivot_index + 1, high))

    return arr
    
def partition_random(data, low , high):
    pivot = randrange(low, high)
    data[low], data[pivot] = data[pivot], data[low] 
    return partition(data, low, high)

def quick_sort_random(data, low, high):
    if low < high:
        i = partition_random(data,low,high)
        quick_sort_random(data,low,i-1)
        quick_sort_random(data,i+1,high)
    return data

def heapify(data, n, i):
    largest = i
    while True:
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and data[left] > data[largest]:
            largest = left


        if right < n and data[right] > data[largest]:
            largest = right

        if largest == i:
            break

        data[i], data[largest] = data[largest], data[i]
        i = largest

def heap_sort(data):
    n = len(data)
    for i in range(n//2-1,-1,-1):
        heapify(data, n, i)
    for i in range(n-1,0,-1):
        data[i], data[0] = data[0], data[i]
        heapify(data,i,0)
    return data

def sedgwick_numbers(data):
    x = [1]
    k = 0
    while True :
        if len(data)/(4**(k+1) + 3*2**k + 1) < 2:
            break
        x.append(4**(k+1) + 3*2**k + 1)
        k = k+1
    return x[::-1]

def shell_sort(data):
    x = sedgwick_numbers(data)
    for i in x:
        insertion_sort(data, i)
    return data

def main():
    sys.setrecursionlimit(100000) #default -> 1000

    if len(sys.argv) != 3 or sys.argv[1] != "--algorithm":
        print("Usage: python script.py --algorithm <algorithm_number>")
        sys.exit(1)

    algorithm_number = int(sys.argv[2])

    data = list(map(int,sys.stdin.read().split()))[1:]
    print(data)
    match algorithm_number:
        case 1:
            pass
        #    insertion_sort(data,1)
        case 2:
            shell_sort(data)
        case 3:
        #    selection_sort(data)
            pass
        case 4:
            heap_sort(data)
        case 5:
            quick_sort_left(data,0,len(data)-1)
        case 6:
            quick_sort_random(data,0,len(data)-1)
            
if __name__ == "__main__":
    main()