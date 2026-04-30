l, r = 0.0, 2.0
for _ in range(100):
    mid = (l + r) / 2.0
    if mid**3 + 4 * mid**2 + mid - 6 < 0:
        l = mid
    else:
        r = mid
print(f"{l:.10f}")