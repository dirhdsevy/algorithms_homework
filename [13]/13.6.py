import sys


def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    line = data[0]

    operators = {"+", "-", "*", "/"}
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
    stack = []

    for char in reversed(line):
        if char not in operators:
            stack.append((char, 10))
        else:
            op1, p1 = stack.pop()
            op2, p2 = stack.pop()

            p_curr = precedence[char]

            left = f"({op1})" if p1 < p_curr else op1

            if p2 < p_curr:
                right = f"({op2})"
            elif p2 == p_curr:
                if char in ("-", "/"):
                    right = f"({op2})"
                else:
                    right = op2
            else:
                right = op2

            stack.append((f"{left}{char}{right}", p_curr))

    if stack:
        print(stack[0][0])


if __name__ == "__main__":
    solve()
