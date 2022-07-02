#LinearSearch
l1=[345,23,43,2,42,55,4,54,64,53]
t1=45
def linearSearch(l1,t1):
    i=t1
    for i in l1:
        if i==t1:
            index=l1.index(i)
            print(index)
        else:
            print("element not found")
            return False
linearSearch(l1,t1)