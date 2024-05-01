#6)implement a sequential search
list=[1,3,2,6,5,7]
key=int(input('enter the key to be searched'))
def search(list,key):
    for i in range(len(list)):
        if key==list[i]:
            print('key found at index',i)
            break
    else:
        print('key not found')
search(list,key)