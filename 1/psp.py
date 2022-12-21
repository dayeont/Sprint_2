def psp(n: int, l_sum:int = 0, r_sum: int = 0, s: str = '') -> str:
    if (l_sum != n) or (r_sum != n):
        if l_sum < n:
            psp(n, l_sum+1, r_sum, s + '(')
        if r_sum < l_sum:
            psp(n, l_sum, r_sum+1, s + ')')
    else:
        print(s)


psp(int(input()))
