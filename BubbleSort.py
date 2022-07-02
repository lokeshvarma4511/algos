l1=[12,1,43,67,4,19,5]

def bubbleS(lis):
    l=len(lis)-1
    for i in range(l):
        for j in range(0,l):
            if lis[j]<lis[j+1]:
                continue
            else:
                lis[j],lis[j+1]=lis[j+1],lis[j]

        slis=lis.sort()
        if lis==slis:
            break
    print(f"sorted list using bubble sort,{lis}")

bubbleS(l1)
print("completed")