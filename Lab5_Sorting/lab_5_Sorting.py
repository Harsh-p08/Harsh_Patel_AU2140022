# -*- coding: utf-8 -*-
"""Lab_5_Sorting

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12Sur8tjW0d3bAz0ReZucHrLWTrUEHXQ7

Harsh Dineshkumar Patel

AU2140022

DSA Section_1
"""

#Program 1

array = [1,5,2,3,4]

def Bubblesort(a):

  l = len(a)
  
  for i in range(0,l):
      check = 0
      for j in range(0,l-i-1):

          if a[j] > a[j+1]:
            tmp = a[j]
            a[j] = a[j+1]
            a[j+1] = tmp
            check += 1
          
      if check==0:
        return a
  return a    
   
Bubblesort(array)

#Program 2

array = [ 9,6,12,4,1,7]

def Selectionsort(a):

   l = len(a)

   for i in range(0,l):
      mini=i
      
      for j in range(i+1,l):
         if a[mini] > a[j]:
           mini=j
      tmp = a[i]
      a[i] = a[mini]
      a[mini] = tmp
   return a

Selectionsort(array)

#Program 3 

array = [5,1,4,6,9,3,2]

def binarySearch(a, x,low,high):
    if low == high:
        if a[low] > x:
            return low
        else:
            return low+1
  
    if low > high:
        return low
  
    mid = (low+high)//2
    if a[mid] < x:
        return binarySearch(a, x, mid+1, high)
    elif a[mid] > x:
        return binarySearch(a, x, low, mid-1)
    else:
        return mid

def insertion_sort_binary(a):
    for i in range(len(a)):
        j = i-1
        tmp = a[i]
        loc = binarySearch(a, tmp,0,j)
        while (j >= loc):
            a[j + 1] = a[j]
            j-=1
        a[j + 1] = tmp
    return a


def InsertionSort(a):
  
    l = len(a)
    for i in range(0,l):
        value = a[i]
        p = i
        while p>0 and value < a[p-1]:
            a[p]=a[p-1]
            p = p-1
        a[p] = value
    return a


print(InsertionSort(array))
insertion_sort_binary(array)

#Program 4

import timeit

Best_Case =[1,2,3,4]
Worst_Case =[4,3,2,1]

def insertion_sort(a):
  
    l = len(a)
    for i in range(0,l):
        value = a[i]
        p = i
        while p>0 and value < a[p-1]:
            a[p]=a[p-1]
            p = p-1
        a[p] = value
    return a

def selection_sort(a):

  for i in range(len(a)):
    mini = i
    for j in range(i+1,len(a)):
      if(a[mini]>a[j]):
        mini = j
    a[i],a[mini]=a[mini],a[i]
  return a

print("Best Case:[1,2,3,4]")
print("Time selsection sort:",timeit.timeit("selection_sort([1,2,3,4])", setup="from __main__ import selection_sort"))
print("Time insertion sort:",timeit.timeit("insertion_sort([1,2,3,4])", setup="from __main__ import insertion_sort"))

print(' ')

print("Worst Case is [4,3,2,1]")
print("Time selsection sort:",timeit.timeit("selection_sort([4,3,2,1])", setup="from __main__ import selection_sort"))
print("Time insertion sort:",timeit.timeit("insertion_sort([4,3,2,1])", setup="from __main__ import insertion_sort"))

#Program 5


def mergeSortedSubseq( theSeq, left, right, end, tmpArray ):

  a=left
  b=right
  m=0

  while a < right and b < end:
    if theSeq[a] < theSeq[b] :
      tmpArray[m] = theSeq[a]
      a += 1
    else :
      tmpArray[m] = theSeq[b]
      b += 1

    m += 1
    

  while a < right :
    tmpArray[m] = theSeq[a]
    a += 1
    m += 1

  while b < end:
    tmpArray[m] = theSeq[b]
    b += 1
    m += 1
    
  for i in range(end-left):
    theSeq[i+left] = tmpArray[i]

def recMergeSort( theSeq, first, last, tmpArray ):

  if first == last :
    return;
  else :
    
    mid = (first + last) // 2
    
  recMergeSort( theSeq, first, mid, tmpArray )
  recMergeSort( theSeq, mid+1, last, tmpArray )

  mergeSortedSubseq( theSeq, first, mid+1, last+1, tmpArray )


def mergeSort( theSeq ): 
    n = len( theSeq )
   
    tmpArray = [-1]*n
    recMergeSort( theSeq, 0, n-1, tmpArray )
    return(tmpArray)

mergeSort([7,1,5,9,21,14])

#Program 6

array = [7,1,3,14,22,9,8]

def quick_Sort(arr,L,H):
    
    if L >= H:
        return
    m = (L+H) // 2
    pivot = arr[m]
    i = L-1
    j = H+1
    while(1):
        while(1):
            i+=1
            if arr[i] >= pivot:
                break
        while(1):
            j-=1
            if arr[j] <= pivot:
                break
        if i >=j :
            break
        arr[i],arr[j] = arr[j],arr[i]
    quick_Sort(arr,L,j)
    quick_Sort(arr,j+1,H)
    return arr

print(quick_Sort(array,0,len(array)-1))

#Program 7

import random

array = [7,2,4,6,9,14,21]

def quick_Sort(arr,L,H):
    if(L < H):
        p = partition(arr,L, H)
        quickSort(arr,L,p-1)
        quickSort(arr,p+1,H)
    return arr

def partition(arr,L,H):
    randp = random.randrange(L,H)
    arr[L], arr[randp] = arr[randp], arr[L]
    p = L
    i = L + 1
    for j in range(L + 1, H + 1):
        if arr[j] <= arr[p]:
            arr[i] , arr[j] = arr[j] , arr[i]
            i += 1
    arr[p] , arr[i - 1] = arr[i - 1] , arr[p]
    p = i - 1
    return p
    
print(quick_Sort(array,0,len(array)-1))

#Program 8

array  = [7,4,8,9,3,1,14]

def CountSort(a,p): 
    l = len(a)
    r = [None]*l
    count = [0]*10
    for i in range (0,l):
        i_p = a[i]//p 
        count[i_p%10] += 1
    for i in range(1,10):
        count[i] += count[i-1]
    i = l-1
    while i>=0:
        i_p = a[i]//p
        r[count[i_p%10]-1] = a[i]
        count[i_p%10] -= 1
        i -= 1
    for i in range(0,l):
        a[i] = r[i]

def Radix_Sort(a):
    max_e = max(a) 
    p = 1
    while max_e//p > 0:
        CountSort(a,p)
        p *= 10
    return a

print(Radix_Sort(array))
