from collections import deque
import sys

def main():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
        
    n = int(input_data[0].strip())
    p1 = deque(map(int, input_data[1].split()))
    p2 = deque(map(int, input_data[2].split()))

    moves = 0
    max_moves = 2 * 10**5

    while p1 and p2 and moves < max_moves:
        moves += 1
        c1 = p1.popleft()
        c2 = p2.popleft()

        # Визначаємо переможця раунду за правилами
        if c1 == 0 and c2 == n - 1:
            p1_win = True
        elif c2 == 0 and c1 == n - 1:
            p1_win = False
        else:
            p1_win = c1 > c2

        # Переможець завжди кладе спочатку c1, потім c2
        if p1_win:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c1)
            p2.append(c2)

    if not p1:
        print(f"second {moves}")
    elif not p2:
        print(f"first {moves}")
    else:
        print("draw")

if __name__ == '__main__':
    main()