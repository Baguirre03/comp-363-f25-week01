def min_span_tree(G):
    T = create_edgeless_copy(G)
    print(T)
    components = component_count(T)
    while components > 1:
        c1 = components[0]
        c2 = components[1]

        components = component_count(T)

    return T


def create_edgeless_copy(G) -> list[list]:
    """
    Return edgeless copy of adjacency matrix
    G[0][0] representing no connection
    1 representing a connection
    """
    LOCAL_INFINITY = G[0][0]
    n = len(G)
    m = len(G[0])
    return [[LOCAL_INFINITY for _ in range(m)] for _ in range(n)]


def component_count(T) -> int:
    """
    Finds the current amount of disconnected componenets in our graph
    """
    res = []
    for vertex in range(len(T)):
        reach = reachability_of(vertex, T)
        res.append(reach)
    return res


def reachability_of(s: int, G) -> list[int]:
    LOCAL_INFINITY = G[0][0]
    reach = []  # return object
    bag = [s]  # place to store which vertex to visit
    while bag:
        v = bag.pop()
        if v not in reach:
            reach.append(v)
            for u in range(len(G)):
                if G[v][u] != LOCAL_INFINITY:
                    bag.append(u)
    return reach


def find_safe_edge(component_one, component_two) -> int:
    """
    Scans every edge between vertices in two different components
    Returns the smallest one
    """


graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0],
]

min_span_tree(graph)
