'''

quickselect.py

'A' variable should contain list of values in initial order

Usage: python3 quickselect.py

This program takes in an ordered list A and finds the kth smallest element using
Quicksort and Lomuto partitioning.

Program also prints to console intermediary steps (lomuto partitions) and related variables

Based on pseudocode from Introduction to the Design and Analysis of Algorithms (3rd Ed.)
'''


A = [51, 10, 43, 86, 92, 15, 38, 77, 76, 41, 22]


def lomuto(A, l, r):
    p = A[l]
    s = l
    for i in range(l+1, r+1):
        if A[i] < p:
            print(f"{A[i]} < {p}")
            s = s + 1
            print(f"S = {s}")
            print(f"Swap {A[s]} {A[i]}")
            A[s], A[i] = A[i], A[s]
            print(A[l:r+1])
    print(A[l:r+1])
    return s

def quickselect(A, l, r, k): 
    print(A)
    s = lomuto(A, l, r)
    print(f"S = {s}")
    if s == k - 1:
        return A[s]
    elif s > l + k - 1:
        return quickselect(A, l, s-1, k)
    else:
        return quickselect(A, s+1, r, k)

def main():
    print(f"There are {len(A)} elements in the array.")
    k = int(input("Select the kth smallest element where k = ").strip())
    result = quickselect(A, 0, len(A)-1, k)
    print(f"{result} is the kth smallest element where k = {k}")

if __name__ == "__main__":
    main()