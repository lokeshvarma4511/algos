ind=0
l1=[23,1,32,1,321,3,235,5,4]
n=int(input("enter the number to search:"))
def binaryS(list1,n):
    l=0
    u=len(list1)-1
    while l <=u:
        mid=(l+u)//2
        if n==list1[mid] :
            globals()['ind']=n
            return True
        else:
            if list1[mid]<=n:
                l=mid;
            else:
                u=mid;

if binaryS(l1,n):
    print("element present at position :",ind+1)
else:
    print("element not found")