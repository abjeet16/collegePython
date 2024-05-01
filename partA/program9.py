#9)Implement selection sort
def selection(a):
    for i in range(0,len(a)):
        min=i
        for j in range(i+1,len(a)):
            if a[j]<a[min]:
                min=j
        temp=a[i]
        a[i]=a[min]
        a[min]=temp
    print(a)
a=[2,4,6,-1,0,-5]
selection(a)
