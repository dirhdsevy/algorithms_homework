import sys
import math

INF = 10**9 + 7

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    g = math.gcd(a, b)
    res = (a // g) * b
    return res if res < INF else INF

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    
    gcd_tree = [0] * (2 * n)
    lcm_tree = [0] * (2 * n)
    
    for i in range(n):
        val = int(input_data[i + 1])
        gcd_tree[n + i] = val
        lcm_tree[n + i] = val if val < INF else INF
        
    for i in range(n - 1, 0, -1):
        gcd_tree[i] = math.gcd(gcd_tree[2 * i], gcd_tree[2 * i + 1])
        lcm_tree[i] = lcm(lcm_tree[2 * i], lcm_tree[2 * i + 1])
        
    m = int(input_data[n + 1])
    idx = n + 2
    out = []
    
    for _ in range(m):
        q = int(input_data[idx])
        if q == 1:
            l = int(input_data[idx + 1]) - 1 + n
            r = int(input_data[idx + 2]) - 1 + n
            
            curr_l, curr_r = l, r
            res_gcd = 0
            while curr_l <= curr_r:
                if curr_l % 2 == 1:
                    res_gcd = math.gcd(res_gcd, gcd_tree[curr_l])
                    curr_l += 1
                if curr_r % 2 == 0:
                    res_gcd = math.gcd(res_gcd, gcd_tree[curr_r])
                    curr_r -= 1
                curr_l //= 2
                curr_r //= 2
                
            curr_l, curr_r = l, r
            res_lcm = 0
            first = True
            while curr_l <= curr_r:
                if curr_l % 2 == 1:
                    if first:
                        res_lcm = lcm_tree[curr_l]
                        first = False
                    else:
                        res_lcm = lcm(res_lcm, lcm_tree[curr_l])
                    curr_l += 1
                if curr_r % 2 == 0:
                    if first:
                        res_lcm = lcm_tree[curr_r]
                        first = False
                    else:
                        res_lcm = lcm(res_lcm, lcm_tree[curr_r])
                    curr_r -= 1
                curr_l //= 2
                curr_r //= 2
                
                if res_lcm > res_gcd:
                    break

            if res_gcd < res_lcm:
                out.append("wins")
            elif res_gcd > res_lcm:
                out.append("loser")
            else:
                out.append("draw")
        else:
            pos = int(input_data[idx + 1]) - 1 + n
            val = int(input_data[idx + 2])
            
            gcd_tree[pos] = val
            lcm_tree[pos] = val if val < INF else INF
            
            p = pos // 2
            while p > 0:
                gcd_tree[p] = math.gcd(gcd_tree[2 * p], gcd_tree[2 * p + 1])
                lcm_tree[p] = lcm(lcm_tree[2 * p], lcm_tree[2 * p + 1])
                p //= 2
                
        idx += 3
        
    print('\n'.join(out))

if __name__ == '__main__':
    main()