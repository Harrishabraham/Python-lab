stack=[]
while True:
    print("1.Push")
    print("2.pop")
    print("3.Peek")
    print("4.Display")
    print("5.Exit")
    choice=int(input("Enter your choice"))
    if choice==1:
        item=(input("Enter book to push :"))
        stack.append(item)
        print(item,"Book is Inserted into stack")
    elif choice==2:
        if len(stack)==0:
            print("Stack is empty ")
        else:
            print("Deleted book:",stack.pop())
    elif choice==3:
        if len(stack)==0:
            print("Stack is empty")
        else:
            print("Top book",stack[-1])
    elif choice==4:
        if len(stack)==0:
            print("Stack is empty")
        else:
            print("stack books:",stack)
    elif choice==5:
        print("Programme ended")
        break
    else:
        print("Invalid choice")
   
