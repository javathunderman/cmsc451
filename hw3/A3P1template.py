class Kosaraju:
    """
    Author: Peter Li (lih@umd.edu)
    Performs Kosaraju's algorithm on a directed graph and returns a labelling specifying the component of each vertex.

    Usage:
    k = Kosaraju(3)
    k.add_edge(1, 2)
    k.add_edge(2, 1)
    k.add_edge(2, 3)
    labels = k.run_kosaraju()
    Result: labels would be [-1, 1, 1, 0], meaning that vertex 1 and 2 are in component 1 while vertex 3 is in component 0.
    Note that vertex 0 is a dummy vertex so that Kosaraju's algorithm is consistent with the vertex IDs in the input data.
    """
    n: int
    cities: list[set[int]]
    reverse_cities: list[set[int]]

    def __init__(self, n: int):
        """
        Initialize Kosaraju's algorithm

        :param n: the number of vertices
        """
        self.n = n
        self.cities = [set() for _ in range(n + 1)]
        self.reverse_cities = [set() for _ in range(n + 1)]

    def add_edge(self, v1: int, v2: int):
        """
        Add a directed edge to the graph. Note that duplicate insertions are okay.

        :param v1: the numeric id of the starting vertex of the edge
        :param v2: the numeric id of the second vertex of the edge
        """
        self.cities[v1].add(v2)
        self.reverse_cities[v2].add(v1)

    def __dfs1(self):
        """
        Internal method of Kosaraju's algorithm. Do not invoke this directly in your solution to problem A.
        Performs an iterative DFS on the transpose graph and returns the vertices in ascending finish time.
        """
        n = self.n
        dfs_order: list[int] = []
        visited = [False] * (n + 1)

        # simulate a recursive algorithm using a stack
        # note that both the vertex itself and the list of its untraversed neighbors need to be tracked
        stack: list[tuple[int, list[int]]]
        def stack_push(vertex: int):
            stack.append((vertex, list(self.reverse_cities[vertex])))
            visited[vertex] = True

        for i in range(1, n+1):
            if visited[i]:
                continue
            # perform a DFS on every unvisited vertex
            stack = []
            stack_push(i)
            while len(stack) > 0:
                top, neighbors = stack[-1]
                # keep visiting its neighbors
                while len(neighbors) > 0:
                    neighbor = neighbors.pop()
                    if not visited[neighbor]:
                        stack_push(neighbor)
                        break
                else:
                    # all neighbors visited; we are done with this vertex
                    stack.pop()
                    dfs_order.append(top)
        return dfs_order

    def __dfs2(self, dfs_order: list[int]) -> list[int]:
        """
        Internal method of Kosaraju's algorithm. Do not invoke this directly in your solution to problem A.
        Given a list of vertices in descending finish time, this function performs iterative DFS to determine the label of each vertex.
        """
        n = self.n
        labels: list[int] = [-1 for _ in range(n + 1)]
        visited = [False for _ in range(n + 1)]
        component_counter = -1

        def iterative_dfs(start_vertex: int):
            """
            Helper function for `__dfs2`. Runs iterative DFS on a starting vertex to
             (1) marks all vertices in its component as visited
             (2) label all vertices of its component

            :param start_vertex: an arbitrary vertex in an unvisited component
            """
            stack: list[int] = [start_vertex]
            visited[start_vertex] = True
            while len(stack) > 0:
                vertex = stack.pop()
                labels[vertex] = component_counter
                for neighbor in self.cities[vertex]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)

        # perform DFS in the order provided
        for v in dfs_order:
            if not visited[v]:
                component_counter += 1
                iterative_dfs(v)

        return labels

    def run_kosaraju(self) -> list[int]:
        """
        Runs Kosaraju's algorithm on the graph and returns a labelling of all vertices.
        See the documentation in the beginning of this class for an example.
        """
        dfs_order = self.__dfs1()
        dfs_order.reverse()
        return self.__dfs2(dfs_order)
