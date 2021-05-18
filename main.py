from random import randint

import matplotlib
from matplotlib import pyplot as plt

matplotlib.use('TkAgg')
indices = []
for i in range(25):
    indices.append(i)


def update_plot(arr):
    plt.title(function)
    plt.bar(indices, arr)
    plt.draw()
    plt.pause(0.0001)
    plt.clf()


def selection_sort(arr):
    update_plot(arr)
    indexing_length = range(0, len(arr) - 1)
    for i in indexing_length:
        min_value = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_value]:
                min_value = j
        if min_value != i:
            arr[min_value], arr[i] = arr[i], arr[min_value]
            update_plot(arr)
    update_plot(arr)
    return arr


def bubble_sort(arr):
    update_plot(arr)
    for i in range(len(arr) - 1):
        entered = False
        for j in range(len(arr) - i - 1):
            if arr[j + 1] < arr[j]:
                entered = True
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                update_plot(arr)
        if not entered:
            break
    update_plot(arr)


def insertion_sort(arr):
    update_plot(arr)
    for i in range(1, len(arr)):
        j = i - 1
        entered = False
        temp = arr[i]
        while temp < arr[j] and j >= 0:
            entered = True
            arr[j + 1] = arr[j]
            j -= 1
            update_plot(arr)
        if entered:
            arr[j + 1] = temp
            update_plot(arr)


def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


def heapify(arr, n, i):
    left = 2 * i + 1
    right = 2 * i + 2
    max = i
    if left < n:
        if arr[left] > arr[i]:
            max = left
        else:
            max = i

    if right < n:
        if arr[right] > arr[max]:
            max = right

    if max != i:
        arr[i], arr[max] = arr[max], arr[i]
        update_plot(arr)
        heapify(arr, n, max)


def heap_sort(arr):
    update_plot(arr)
    build_max_heap(arr)
    n = len(arr)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        update_plot(arr)
        n = n - 1
        heapify(arr, n, 0)
    update_plot(arr)


sorting_functions = {'Insertion Sort': insertion_sort, 'Bubble Sort': bubble_sort, 'Selection Sort': selection_sort,
                     'Heap Sort': heap_sort}
arr = []
for j in range(25):
    arr.append(randint(0, 10000))
for function in sorting_functions.keys():
    temp = arr.copy()
    sorting_functions[function](temp)
input('Press any button to exit:')