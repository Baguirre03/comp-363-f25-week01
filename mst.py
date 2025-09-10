def min_span_tree(G):
    T: list[list[int]] = create_edgeless_copy(G)
    component_count, component_map = count_components(T)
    while component_count > 2:
        component_count, component_map = count_components(T)
        row, column, weight = find_smallest_edge(G, T)
        T[row][column] = weight
        T[column][row] = weight

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
    return [[LOCAL_INFINITY for c in range(m)] for r in range(n)]


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
    components_map: list[int] = [None] * len(T)
    visited: set[int] = set()
    for v in range(len(T)):
        if v not in visited:
            count += 1
            visited.add(v)
            reach = reachability_of(v, T)
            for vertex in reach:
                components_map[vertex] = count
            visited.update(reach)
    return count, components_map


def reachability_of(s: int, G: list[list[int]]) -> list[int]:
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


def find_smallest_edge(G, T):
    smallest = float("inf")
    row = None
    col = None
    for r in range(len(G)):
        for c in range(len(G)):
            if G[r][c] < smallest and G[r][c] != G[0][0] and T[r][c] == 0:
                row = r
                col = c
                smallest = G[r][c]
    return row, col, smallest


graph = [
    [0, 4, 0, 0, 9],
    [4, 0, 3, 7, 0],
    [0, 3, 0, 2, 5],
    [0, 7, 2, 0, 6],
    [9, 0, 5, 6, 0],
]

print(min_span_tree(graph))
