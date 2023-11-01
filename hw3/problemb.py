from segtree import SegTree

# example code for range minimum queries
n, q = map(int, input().split())
arr = list(map(int, input().split()))
segtree = SegTree(arr)

for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        # update the value at index a to b
        segtree.update(a, b)
    else:
        # query the minimum value in the interval [a,b)
        print(segtree.query(a, b).val)