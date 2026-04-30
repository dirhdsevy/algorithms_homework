l, r = 0.0, 10.0
for _ in range(100):
    mid = (l + r) / 2.0
    if mid**3 + mid - 4 < 0:
        l = mid
    else:
        r = mid
print(f"{l:.10f}")