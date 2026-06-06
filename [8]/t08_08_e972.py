n = int(input())
times = []
for _ in range(n):
    h, m, s = map(int, input().split())
    times.append([h, m, s])

for i in range(n - 1):
    min_idx = i
    for j in range(i + 1, n):
        if times[j][0] < times[min_idx][0]:
            min_idx = j
        elif times[j][0] == times[min_idx][0]:
            if times[j][1] < times[min_idx][1]:
                min_idx = j
            elif times[j][1] == times[min_idx][1]:
                if times[j][2] < times[min_idx][2]:
                    min_idx = j
                    
    times[i], times[min_idx] = times[min_idx], times[i]

for t in times:
    print(t[0], t[1], t[2])