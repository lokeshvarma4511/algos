list=[23,41,43,5,2,432,412]

def selectionSort(list1):
    for i in range(0,len(list1)):
        list2=list1[i:len(list1)]
        m = min(list2)
        mi=list1.index(m)
        list1[i],list1[mi]=list1[mi],list1[i]
    print(list1)
selectionSort(list)