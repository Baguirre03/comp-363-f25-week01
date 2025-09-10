def min_span_tree(G):
    T: list[list[int]] = create_edgeless_copy(G)
    component_count, component_map = count_components(T)
    print(component_count, component_map)
    while component_count > 1:
        component_count, component_map = component_count(T)
        # find first node with mapping to component 1 and component 2
        c1: int = component_map.index(1)
        c2: int = component_map.index(2)
        find_safe_edge(c1, c2)

        # do this by search componenet map to find first index of 1 and second instance of 2

    return T


def create_edgeless_copy(G: list[list[int]]) -> list[list]:
    """
    Return edgeless copy of adjacency matrix
    G[0][0] representing no connection
    1 representing a connection
    """
    LOCAL_INFINITY = G[0][0]
    n: int = len(G)
    m: int = len(G[0])
    return [
        [LOCAL_INFINITY if G[r][c] == LOCAL_INFINITY else 1 for c in range(m)]
        for r in range(n)
    ]


def count_components(T: list[list[int]]) -> tuple[int, list[int]]:
    """
    Finds the current amount of disconnected componenets in our graph
    Args:
        T (int): (edgeless graph)
    Returns:
        [0]: count of components
        [1]: actually list mapping vertex (index) -> component
    """
    count: int = 0
    components: list[int] = [None] * len(T)
    visited: set[int] = set()
    for v in range(len(T)):
        if v not in visited:
            count += 1
            visited.add(v)
            reach = reachability_of(v, T)
            for vertex in reach:
                components[vertex] = count
            visited.update(reach)
    return count, components


def reachability_of(s: int, G) -> list[int]:
    """ """
    LOCAL_INFINITY = G[0][0]
    reach: list[int] = []  # return object
    visit_next: list[int] = [s]  # place to store which vertex to visit
    while visit_next:
        v = visit_next.pop()
        if v not in reach:
            reach.append(v)
            for u in range(len(G)):
                if G[v][u] != LOCAL_INFINITY:
                    visit_next.append(u)
    return reach


def find_safe_edge(component_one, component_two) -> int:
    """
    Scans every edge between vertices in two different components
    Returns the smallest one
    """
    return 0


graph = [
    [0, 2, 0, 0, 0],
    [2, 0, 3, 0, 0],
    [0, 3, 0, 0, 0],
    [0, 0, 0, 0, 9],
    [0, 0, 0, 9, 0],
]


min_span_tree(graph)
