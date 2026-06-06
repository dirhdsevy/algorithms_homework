import sys

stack = []

for line in sys.stdin:
    parts = line.split()
    if not parts:
        continue
    
    cmd = parts[0]
    
    if cmd == "push":
        n = int(parts[1])
        stack.append(n)
        print("ok")
        
    elif cmd == "pop":
        if len(stack) > 0:
            print(stack.pop())
        else:
            print("error")
            
    elif cmd == "back":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print("error")
            
    elif cmd == "size":
        print(len(stack))
        
    elif cmd == "clear":
        stack.clear()
        print("ok")
        
    elif cmd == "exit":
        print("bye")
        break