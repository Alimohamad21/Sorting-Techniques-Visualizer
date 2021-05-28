import time
from random import randint
from threading import Thread

import matplotlib
from matplotlib import pyplot as plt
from playsound import playsound

matplotlib.use('TkAgg')
indices = []
test_array_length = 25
for i in range(test_array_length):
    indices.append(i)


def play(file):
    Thread(target=playsound, args=(file,), daemon=True).start()


def update_plot(arr, i=-1, j=-1, last=False, first=False):
    global iterations
    global function
    colors = test_array_length * ['#1f77b4']
    if i != -1:
        colors[i] = '#2ca02c'
    if j != -1:
        colors[j] = '#2ca02c'
    plt.title(f'{function}        Iterations:{iterations}')
    delay = 0.0001
    if last:
        for i in range(test_array_length):
            colors[i] = '#2ca02c'
            plt.title(f'{function}        Iterations:{iterations}')
            plt.bar(indices, arr, color=colors)
            plt.pause(delay)
            plt.draw()
            if i == test_array_length - 1:
                plt.pause(1000 * delay)
            plt.clf()
            play('sounds/sound2.wav')
    else:
        plt.bar(indices, arr, color=colors)
        plt.draw()
        plt.pause(delay)
        plt.clf()
        if not first:
            play('sounds/sound1.wav')


def selection_sort(arr):
    global iterations
    indexing_length = range(0, len(arr) - 1)
    for i in indexing_length:
        min_value = i
        for j in range(i + 1, len(arr)):
            iterations += 1
            if arr[j] < arr[min_value]:
                min_value = j
        if min_value != i:
            arr[min_value], arr[i] = arr[i], arr[min_value]
            if visual:
                update_plot(arr, min_value, i)
    return arr


def bubble_sort(arr):
    global iterations
    for i in range(len(arr) - 1):
        entered = False
        for j in range(len(arr) - i - 1):
            iterations += 1
            if arr[j + 1] < arr[j]:
                entered = True
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                if visual:
                    update_plot(arr, j, j + 1)
        if not entered:
            break


def insertion_sort(arr, left=-10, right=-10):
    global iterations
    if left == -10 and right == -10:
        values = range(1, len(arr))
    else:
        values = range(left + 1, right + 1)
    for i in values:
        j = i - 1
        entered = False
        temp = arr[i]
        while temp < arr[j] and j >= 0:
            iterations += 1
            entered = True
            arr[j + 1] = arr[j]
            j -= 1
            if visual:
                update_plot(arr, j, j + 1)
        if entered:
            arr[j + 1] = temp
            if visual:
                update_plot(arr, j + 1)


def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


def heapify(arr, n, i):
    left = 2 * i + 1
    right = 2 * i + 2
    global iterations
    iterations += 1
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
        if visual:
            update_plot(arr, max, i)
        heapify(arr, n, max)


def heap_sort(arr):
    build_max_heap(arr)
    n = len(arr)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        if visual:
            update_plot(arr)
        n = n - 1
        heapify(arr, n, 0)


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        global iterations
        iterations += 1
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            if visual:
                update_plot(arr, i, j)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    if visual:
        update_plot(arr, i=i + 1, j=high)
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def merge(arr, start, mid, end):
    start2 = mid + 1
    if arr[mid] <= arr[start2]:
        return
    while start <= mid and start2 <= end:
        global iterations
        if arr[start] <= arr[start2]:
            start += 1
        else:
            value = arr[start2]
            index = start2
            while index != start:
                iterations += 1
                arr[index] = arr[index - 1]
                if visual:
                    update_plot(arr, index, index - 1)
                index -= 1
            arr[start] = value
            if visual:
                update_plot(arr, start)
            start += 1
            mid += 1
            start2 += 1


def merge_sort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)


def calcMinRun(n):
    r = 0
    while n >= 32:
        r |= n & 1
        n >>= 1
    return n + r


def tim_sort(arr):
    n = len(arr)
    minRun = calcMinRun(n)
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertion_sort(arr, start, end)
    size = minRun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            if mid < right:
                merge(arr, left, mid, right)
        size = 2 * size


sorting_functions = {'Insertion Sort': insertion_sort, 'Bubble Sort': bubble_sort,
                     'Selection Sort': selection_sort,
                     'Merge Sort': merge_sort, 'Heap Sort': heap_sort, 'Quick Sort': quick_sort,
                     }
function = ''
visual = True
iterations = 0


def visualize():
    global iterations
    global function
    global visual
    sorting_functions['Built-in Python sort'] = tim_sort
    visual = True
    arr = []
    for j in range(test_array_length):
        arr.append(randint(0, 100000))
    for function in sorting_functions.keys():
        temp = arr.copy()
        args = [temp]
        if function == 'Quick Sort' or function == 'Merge Sort':
            args.append(0)
            args.append(len(temp) - 1)
        iterations = 0
        update_plot(temp, first=True)
        sorting_functions[function](*args)
        update_plot(temp, last=True)


def plot_runtimes():
    global sorting_functions
    global visual
    visual = False
    sorting_functions['Built-in Python sort'] = sorted
    random_arrays = []
    n = 10
    for i in range(4):
        random_array = []
        for j in range(n):
            random_array.append(randint(-10000, 10000))
        random_arrays.append(random_array)
        n *= 10
    runtimes = dict()
    sizes = []
    for function in sorting_functions.keys():
        runtimes[function] = []
    for i in range(len(random_arrays)):
        size = len(random_arrays[i])
        sizes.append(size)
        print(
            f'\n---------------------------------------------------> ARRAY SIZE:{size} <---------------------------------------------------\n\n')
        for function in sorting_functions.keys():
            temp_inplace = random_arrays[i].copy()
            temp = random_arrays[i].copy()
            if i == 0:  # only prints for size 10 to avoid extremely long prints
                print(f'Array Before {function}:{temp_inplace}\n')
            start_time = time.time()
            if function == 'Built-in Sort':
                args = [temp]
            else:
                args = [temp_inplace]
            if function == 'Quick Sort' or function == 'Merge Sort':
                args.append(0)
                args.append(len(temp_inplace) - 1)
            sorting_functions[function](*args)
            runtime = (time.time() - start_time)
            runtimes[function].append(runtime)
            if i == 0:  # only prints for size 10 to avoid extremely long prints
                if function == 'Built-in Sort':
                    print(f'Array After {function}:{sorting_functions[function](*args)}\n')
                else:
                    print(f'Array After {function}:{temp_inplace}\n')
            print(f'{function} Runtime:{runtime} s\n')
            print('\n\n\n********************************************************************************\n\n\n')
    print(runtimes)
    for function in sorting_functions.keys():
        plt.plot(sizes, runtimes[function])
    function_names = tuple(sorting_functions.keys())
    plt.legend(function_names)
    plt.xlabel('Array Size')
    plt.ylabel('Run time (in seconds)')
    plt.ylim([0, 3])
    plt.show()


plot_runtimes()
visualize()
