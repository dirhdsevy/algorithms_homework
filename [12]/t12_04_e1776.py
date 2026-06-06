import sys

def solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
        
    line_idx = 0
    while line_idx < len(lines):
        line = lines[line_idx].strip()
        if not line:
            line_idx += 1
            continue
            
        n = int(line)
        if n == 0:
            break
            
        line_idx += 1
        
        while line_idx < len(lines):
            sub_line = lines[line_idx].strip()
            if sub_line == "0":
                print()
                line_idx += 1
                break
                
            target = list(map(int, sub_line.split()))
            
            stack = []
            current_train = 1
            possible = True
            
            for coach in target:
                while current_train <= n and (not stack or stack[-1] != coach):
                    stack.append(current_train)
                    current_train += 1
                
                if stack and stack[-1] == coach:
                    stack.pop()
                else:
                    possible = False
                    break
            
            if possible:
                print("Yes")
            else:
                print("No")
                
            line_idx += 1

if __name__ == '__main__':
    solve()