import math

l, r = 1.6, 3.0
for _ in range(100):
    mid = (l + r) / 2.0
    if math.sin(mid) - mid / 3 > 0:
        l = mid
    else:
        r = mid
print(f"{l:.10f}")