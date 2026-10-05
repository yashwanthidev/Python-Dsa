def linearsearch(arr,el):
  for i in range(len(arr)):
    if arr[i]==el:
      print(f"Element is found at {i}")
      return 
  print("Element not found")

def linearsearch1(arr,el):
  for i in range(len(arr)):
    if arr[i]==el:
      return i 
  return -1

def linearsearch2(ar,el):
  arr=[]
  for i in range(len(ar)):
    if ar[i]==el:
      arr.append(i)
  return arr


a=[12,11,44,32,23,1,8,5,23]
linearsearch(a,23)
print(linearsearch1(a,23))
res=linearsearch2(a,23)
for i in res:
  print(i,end=" ")
