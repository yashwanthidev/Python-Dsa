def binarysearch(arr, el):
  left=0
  right=len(arr) - 1
  while left<=right:
    mid=(left + right)// 2
    if left==mid:
      return -1
    if arr[mid]==el:
      return mid
    elif arr[mid]<el:
      left=mid
    else:
      right=mid

a = [2, 4, 5, 6, 12, 16, 34, 22]
a.sort()
print(binarysearch(a, 22))