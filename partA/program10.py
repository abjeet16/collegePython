#implement stack using list
def push():
    n=int(input('enter the element to be inserted into stack'))
    if len(stack)==0:
        stack.append(n)
    else:
        stack.insert(0,n)
    print(n,'is inserted to stack')
def pop():
    if len(stack)==0:
        print("stack is empty")
    else:
        print(stack[0],'is deleted from stack')
        del stack[0]
def display():
    if len(stack)==0:
        print('stack is empty')
    else:
        print('elements of stack')
        for ele in stack:
            print(ele)
        print('top of the stack is',stack[0])
stack=list()
while(1):
    print('enter the option 1.push\n 2.pop\n 3.display\n 4.exit')
    str=input()
    if str=='1':
        print('push operation')
        push()
    elif str=='2':
        print('pop operation')
        pop()
    elif str=='3':
        print('display')
        display()
    else:
        print('exit')
        break