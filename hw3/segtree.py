class TreeNode:
    # this is an example of a segtree node for min queries
    def __init__(self, val):
        # the data of the segtree
        self.val = val

    def op(self, other):
        # the binary operation of the segtree
        return TreeNode(min(self.val,other.val))

    def default(self):
        # the default value of the segtree
        return TreeNode(int(1e18))

class SegTree:
    # iterative segtree (different from the recursive one taught in class)
    # this segtree is 0-indexed
    def __init__(self, arr):
        self.n = len(arr)
        # the segtree array
        self.tree = [TreeNode(None)] * (2 * self.n)
        self.build(arr)

    def build(self, arr):
        # build the segtree
        for i in range(self.n):
            self.tree[i + self.n] = TreeNode(arr[i])
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2].op(self.tree[i * 2 + 1])

    def update(self, i, val):
        # update the segtree
        i += self.n
        self.tree[i] = TreeNode(val) # set the value of the leaf to be val
        while i > 1:
            i //= 2
            self.tree[i] = self.tree[i * 2].op(self.tree[i * 2 + 1])

    def query(self, l, r):
        # query the segtree with interval [l,r)
        l += self.n
        r += self.n
        leftNode = TreeNode.default(self);
        rightNode = TreeNode.default(self);
        while l < r:
            if l % 2 == 1:
                leftNode = leftNode.op(self.tree[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                rightNode = self.tree[r].op(rightNode)
            l //= 2
            r //= 2

        return leftNode.op(rightNode)

