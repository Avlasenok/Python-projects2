def c_nk(n, k):
    if k == 0:
        return 1
    if k > n:
        return 0
    return c_nk(n - 1, k) + c_nk(n - 1, k - 1)


n, k = map(int, input().split())
print(c_nk(n, k))
