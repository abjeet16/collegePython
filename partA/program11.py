#11.Read and Write into a file.

f1=open("abc.txt","w")
f1.write("welcome to python")
list1=["\n hello" ,"\n python " ,"\n world"]
f1.writelines(list1)
f1=open("abc.txt","a")
f1.write("\n programming")
f1=open("abc.txt","r")
print(f1.read(2))
print(f1.readline())
print(f1.readline())
print(f1.readlines())
f1.close()