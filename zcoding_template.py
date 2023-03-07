"""Things to do if you are stuck:-
1.Read the problem statement again, maybe you've read something wrong.
2.See the explanation for the sample input .
3.If the solution is getting too complex in cases where no. of submissions 
  are high ,then drop that idea because there is something simple which you are
  missing.
4.Check for runtime errors if unexpected o/p is seen.
5.Check on edge cases before submitting.
6.Ensure that you have read all the inputs before returning for a test case.
7.Try to think of brute force first if nothing is striking.
8.Take more examples
9.Don't give up , maybe you're just one statement away! """
# pyrival orz
import collections
import os
import sys
import math
from io import BytesIO, IOBase


input = sys.stdin.readline
############ ---- Input Functions ---- ############


def inp():
    return (int(input()))


def inlt():
    return (list(map(int, input().split())))


def insr():
    s = input()
    return (list(s[:len(s) - 1]))


def invr():
    return (map(int, input().split()))

############ ---- Dijkstra with path ---- ############


def dijkstra(start, distance, path, n):
    # requires n == number of vertices in graph,
    # adj == adjacency list with weight of graph

    # To keep track of vertices that are visited
    visited = [False for _ in range(n)]
    distance[start] = 0  # distance of start node from itself is 0

    for i in range(n):
        v = -1  # Initialize v == vertex from which its neighboring vertices' distance will be calculated
        for j in range(n):
            # If it has not been visited and has the lowest distance from start
            if not visited[v] and (v == -1 or distance[j] < distance[v]):
                v = j

        if distance[v] == math.inf:
            break

        visited[v] = True  # Mark as visited

        for edge in adj[v]:
            destination = edge[0]  # Neighbor of the vertex
            weight = edge[1]  # Its corresponding weight

            # If its distance is less than the stored distance
            if distance[v] + weight < distance[destination]:
                distance[destination] = distance[v] + \
                    weight  # Update the distance
                path[destination] = v  # Update the path


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def pow2(n):
    p = 0
    while n > 1:
        n //= 2
        p += 1
    return p


def isPrime(n):
    if n == 1:
        return False
    else:
        root = int(n ** 0.5)
        root += 1
        for i in range(2, root):
            if n % i == 0:
                return False
        return True
    

def ispalindrome(s):

	return s == s[::-1]


def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
mod = 1000000007
def expo(a, b) :
    if not b : return 1
    v = expo(a, b//2)
    v = (v * v) % mod
    if b%2 : v = (v * a) % mod
    return v



def maxPrimeFactors(n):
    maxPrime = -1
    while n % 2 == 0:
        maxPrime = 2
        n >>= 1
    for i in range(3, int(M.sqrt(n)) + 1, 2):
        while n % i == 0:
            maxPrime = i
            n = n / i
    if n > 2:
        maxPrime = n
    return int(maxPrime)




def lcm(a, b):
    return (a*b)//gcd(a, b)


def ncr(n, r):
    return math.factorial(n)//(math.factorial(n-r)*math.factorial(r))


def npr(n, r):
    return math.factorial(n)//math.factorial(n-r)


def kadane(x):  # maximum sum contiguous subarray
    sum_so_far = 0
    current_sum = 0
    for i in x:
        current_sum += i
        if current_sum < 0:
            current_sum = 0
        else:
            sum_so_far = max(sum_so_far, current_sum)
    return sum_so_far


def primefactors(n):
    factors = []
    while (n % 2 == 0):
        factors.append(2)
        n //= 2
    for i in range(3, int(sqrt(n))+1, 2):  # only odd factors left
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:  # incase of prime
        factors.append(n)
    return factors
def seive(n):
    primes = [True]*(n+1)
    ans = []

    for i in range(2, n):
        if not primes[i]:
            continue

        j = 2*i
        while j <= n:
            primes[j] = False
            j += i

    for p in range(2, n+1):
        if primes[p]:
            ans += [p]

    return ans


def factors(n):
    factors = []

    x = 1
    while x*x <= n:

        if n % x == 0:
            if n // x == x:
                factors.append(x)
            else:
                factors.append(x)
                factors.append(n//x)

        x += 1

    return factors


# Functions: list of factors, seive of primes, gcd of two numbers,
# lcm of two numbers, npr, ncr


def simulation(a, b):
    na, nb = len(a), len(b)
    a = "0"*(max(0, nb - na)) + a
    b = "0"*(max(0, na - nb)) + b
    ans = collections.deque()

    for i in range(len(a)-1, -1, -1):
        add = int(a[i]) + int(b[i])
        ans.appendleft(str(add))

    return list(ans)



BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
def input(): return sys.stdin.readline().rstrip("\r\n")


class SegmentTree:
    def __init__(self, data, default=0, func=lambda a, b: max(a, b)):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len-1).bit_length()

        self.data = [default] * (2 * _size)
        self.data[_size:_size+self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i+i], self.data[i+i+1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx+self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(
                self.data[2 * idx], self.data[2 * idx+1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        if start == stop:
            return self.__getitem__(start)
        stop += 1
        start += self._size
        stop += self._size

        res = self._default
        while start < stop:
            if start & 1:
                res = self._func(res, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res = self._func(res, self.data[stop])
            start >>= 1
            stop >>= 1
        return res

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)


class Graphs:
    def __init__(self):
        self.graph = graphDict(set)

    def add_edge(self, u, v):
        self.graph[u].add(v)
        self.graph[v].add(u)

    def dfs_utility(self, nodes, visited_nodes, colors, parity, level):
        global count
        if nodes == 1:
            colors[nodes] = -1
        else:
            if len(self.graph[nodes]) == 1 and parity % 2 == 0:
                if q == 1:
                    colors[nodes] = 1
                else:
                    colors[nodes] = -1
                    count += 1
            else:
                if parity % 2 == 0:
                    colors[nodes] = -1
                else:
                    colors[nodes] = 1
        visited_nodes.add(nodes)
        for neighbour in self.graph[nodes]:
            new_level = level + 1
            if neighbour not in visited_nodes:
                self.dfs_utility(neighbour, visited_nodes,
                                 colors, level - 1, new_level)

    def dfs(self, node):
        Visited = set()
        color = collections.defaultdict()
        self.dfs_utility(node, Visited, color, 0, 0)
        return color

    def bfs(self, node, f_node):
        count = float("inf")
        visited = set()
        level = 0
        if node not in visited:
            queue.append([node, level])
            visited.add(node)
        flag = 0
        while queue:
            parent = queue.popleft()
            if parent[0] == f_node:
                flag = 1
                count = min(count, parent[1])
            level = parent[1] + 1
            for item in self.graph[parent[0]]:
                if item not in visited:
                    queue.append([item, level])
                    visited.add(item)
        return count if flag else -1
        return False


################### Tree Implementaion ##############
class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(node, lis):
    if node:
        inorder(node.left, lis)
        lis.append(node.data)
        inorder(node.right, lis)
    return lis


def leaf_node_sum(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.data
    return leaf_node_sum(root.left) + leaf_node_sum(root.right)


def hight(root):
    if root is None:
        return -1
    if root.left is None and root.right is None:
        return 0
    return max(hight(root.left), hight(root.right)) + 1


################## Union Find #######################
class UnionFind():
    parents = []
    sizes = []
    count = 0

    def __init__(self, n):
        self.count = n
        self.parents = [i for i in range(n)]
        self.sizes = [1 for i in range(n)]

    def find(self, i):
        if self.parents[i] == i:
            return i
        else:
            self.parents[i] = self.find(self.parents[i])
            return self.parents[i]

    def unite(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j:
            return
        elif root_i < root_j:
            self.parents[root_j] = root_i
            self.sizes[root_i] += self.sizes[root_j]
        else:
            self.parents[root_i] = root_j
            self.sizes[root_j] += self.sizes[root_i]

    def same(self, i, j):
        return self.find(i) == self.find(j)

    def size(self, i):
        return self.sizes[self.find(i)]

    def group_count(self):
        return len(set(self.find(i) for i in range(self.count)))

    def answer(self, extra, p, q):
        dic = collections.Counter()
        for q in range(n):
            dic[self.find(q)] = self.size(q)
        hq = list(dic.values())
        heapq._heapify_max(hq)
        ans = -1
        for z in range(extra + 1):
            if hq:
                ans += heapq._heappop_max(hq)
            else:
                break
        return ans
    

class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)

    
    
    
    
    
def main():
    try:
      
        for _ in range(input()):
            n = int(input())
            
                
          
        v=list(map(int,input().split()))
        count = 0
        print(1223)
        

    except Exception as e:
        print(e)
if __name__ == "__main__":
    main()
