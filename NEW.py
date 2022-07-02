def binary(L1,n):
    min = 0
    max = len(L1)-1
    while min<=max:
        mid = (min+max) // 2
        # print(mid)
        if n==L1[mid]:
            globals()['ind']=mid
            return True
        elif L1[mid]<n:
            min=mid+1
        else:
            max=mid-1
    return False
L1=[20,25,39,61,68, 70 ,79,92,104,120,489]
ind=0
n=int(input("enter the number that to search:"))
# L1=L1.sort()
if binary(L1,n):
    print("element found at:",ind+1)
else:
    print("element not found")

