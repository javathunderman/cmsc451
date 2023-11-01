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


initial_str = input()
input_arr = initial_str.split()
n = int(input_arr[0])
m = int(input_arr[1])
kosarajuObj = Kosaraju(n)
adj_list = {}
cost_dict = {}
pairs = []
for i in range(0, m):
    current_line = input()
    current_arr = current_line.split()
    src = int(current_arr[0])
    dst = int(current_arr[1])
    if (not (src in adj_list.keys())):
        adj_list[src] = []
    pairs.append((src, dst))
    adj_list[src].append(dst)

costs_arr = input().split()
cost_vals = list(map(int, costs_arr))
for i in range(0, m):
    cost_dict[pairs[i]] = cost_vals[i]

for src in adj_list.keys():
    for dst in adj_list[src]:
        # print(f"From {src} to {dst} at cost {cost_dict[(src, dst)]}")
        kosarajuObj.add_edge(src, dst)

labels = kosarajuObj.run_kosaraju()
unique_labels = list(set(labels))
vertex_to_component = dict()
max_component_weight = dict()
intercomponent_edges = dict()
component_to_vertex = dict()
for i in range(0, len(labels)):
    vertex_to_component[i] = labels[i]
    if (labels[i] not in component_to_vertex.keys()):
        component_to_vertex[labels[i]] = []
    component_to_vertex[labels[i]].append(i)

for src in adj_list.keys():
    for dst in adj_list[src]:
        if (vertex_to_component[src] == vertex_to_component[dst]):
            component_label = vertex_to_component[src]
            if not (component_label in max_component_weight.keys()):
                max_component_weight[vertex_to_component[src]] = cost_dict[(src, dst)]
            else:
                max_component_weight[component_label] = max(max_component_weight[component_label], cost_dict[(src, dst)])
        else:
            if not (vertex_to_component[src] in intercomponent_edges.keys()):
                intercomponent_edges[vertex_to_component[src]] = []
            intercomponent_edges[vertex_to_component[src]].append((src, dst))

max_intercomponent_edges = -1
current_component = -1
for key in intercomponent_edges.keys():
    if max_intercomponent_edges < len(intercomponent_edges[key]):
        current_component = key
        max_intercomponent_edges = intercomponent_edges[key]
current_vertex = component_to_vertex[current_component][0]

while (len(adj_list[current_vertex]) != 0):
    for dst in adj_list[current_vertex]:
        if (cost_dict[(current_vertex, dst)] > 0):
            cost_dict[(current_vertex, dst)] -= 1

# I have no idea

