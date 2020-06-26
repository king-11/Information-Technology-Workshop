from sys import stdin, stdout
from random import randint


def quicksort(arr: list, start: int, end: int):
    if(start < end):
        pivot = partition(arr, start, end)
        quicksort(arr, start, pivot-1)
        quicksort(arr, pivot+1, end)


def partition(arr: list, start: int, end: int):
    rand = randint(start, end-1)
    arr[rand], arr[end] = arr[end], arr[rand]

    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[end] = arr[end], arr[i+1]
    return i+1


if __name__ == "__main__":
    a = [int(x) for x in stdin.readline().split()]
    end = len(a)
    quicksort(a, 0, end-1)
    print(a)
