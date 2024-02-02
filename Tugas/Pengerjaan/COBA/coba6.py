from time import perf_counter_ns
import random

def sort_mylist(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i] < list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return list

def bubbleSort(list):
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list

def quickSort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list.pop()

    greater_than_pivot = []
    less_than_pivot = []

    for item in list:
        if item > pivot:
            greater_than_pivot.append(item)
        else:
            less_than_pivot.append(item)
    return quickSort(less_than_pivot) + [pivot] + quickSort(greater_than_pivot)

def insertionSort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i-1
        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key
    return list

def selectionSort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i+1, len(list)):
            if list[min_index] > list[j]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    return list




my_list = random.sample(range(1, 100000), 100)

t1_start = perf_counter_ns()
sort_mylist(my_list)
t1_stop = perf_counter_ns()

t2_start = perf_counter_ns()
quickSort(my_list)
t2_stop = perf_counter_ns()

t3_start = perf_counter_ns()
insertionSort(my_list)
t3_stop = perf_counter_ns()

t4_start = perf_counter_ns()
selectionSort(my_list)
t4_stop = perf_counter_ns()

t5_start = perf_counter_ns()
bubbleSort(my_list)
t5_stop = perf_counter_ns()

print(f"Elapsed time using sort_mylist:   {t1_stop - t1_start}")
print(f"Elapsed time using quickSort:     {t2_stop - t2_start}")
print(f"Elapsed time using insertionSort: {t3_stop - t3_start}")
print(f"Elapsed time using selectionSort: {t4_stop - t4_start}")
print(f"Elapsed time using bubbleSort:    {t5_stop - t5_start}")