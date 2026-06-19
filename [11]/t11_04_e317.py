import sys

sys.set_int_max_str_digits(400000)

def brute_force_multiply(a, b):
    if a < b:
        a, b = b, a
        
    result = 0
    for _ in range(b):
        result += a
    return result

def karatsuba(x, y, depth=0):
    if x < 10 or y < 10:
        return brute_force_multiply(x, y)
    
    if depth >= 3:
        return x * y
    
    m = max(x.bit_length(), y.bit_length()) // 2
    
    x1 = x >> m
    x0 = x & ((1 << m) - 1)
    y1 = y >> m
    y0 = y & ((1 << m) - 1)
    
    z0 = karatsuba(x0, y0, depth + 1)
    z2 = karatsuba(x1, y1, depth + 1)
    z1 = karatsuba(x0 + x1, y0 + y1, depth + 1)
    
    return (z2 << (2 * m)) + ((z1 - z2 - z0) << m) + z0

def main():
    input_data = sys.stdin.read().split()
    if len(input_data) >= 2:
        A = int(input_data[0])
        B = int(input_data[1])
        
        result = karatsuba(A, B)
        print(result)

if __name__ == '__main__':
    main()