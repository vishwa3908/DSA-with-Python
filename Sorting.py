# Selection Sort
def Selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print("Selection Sort")   
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print("\n")

A = [4,3,7,5,1]
Selection_sort(A)     

# Bubble Sort
def Bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("Bubble Sort")
    for i in range(len(arr)):
        print(arr[i],end=" ")

B = [30,20,40,10,60,50]
Bubble_sort(B)
