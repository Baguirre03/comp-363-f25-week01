def min_span_tree(G):
    T: list[list[int]] = create_edgeless_copy(G)
    component_count, component_map = count_components(T)
    while component_count > 2:
        component_count, component_map = count_components(T)
        row, column, weight = find_smallest_edge(component_map, G, T)
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


def find_smallest_edge(component_map, G, T):
    smallest = float("inf")
    row = None
    col = None
    indexes_1 = list(
        filter(
            lambda x: x != -1,
            [index if val == 1 else -1 for index, val in enumerate(component_map)],
        )
    )
    indexes_2 = list(
        filter(
            lambda x: x != -1,
            [index if val == 2 else -1 for index, val in enumerate(component_map)],
        )
    )
    for index_1 in indexes_1:
        for index_2 in indexes_2:
            if (
                G[index_1][index_2] < smallest
                and T[index_1][index_2] == 0
                and G[index_1][index_2] != G[0][0]
            ):
                smallest = G[index_1][index_2]
                row = index_1
                col = index_2
    return row, col, smallest


graphs = [
    [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0],
    ],
    [
        [0, 3, 0, 0, 0, 1],
        [3, 0, 2, 1, 10, 0],
        [0, 2, 0, 3, 0, 5],
        [0, 1, 3, 0, 5, 0],
        [0, 10, 0, 5, 0, 4],
        [1, 0, 5, 0, 4, 0],
    ],
    [
        [0, 2, 3, 0, 6],
        [2, 0, 4, 5, 0],
        [3, 4, 0, 7, 8],
        [0, 5, 7, 0, 9],
        [6, 0, 8, 9, 0],
    ],
    [[0, 1, 4, 0], [1, 0, 2, 6], [4, 2, 0, 3], [0, 6, 3, 0]],
]

for indx, graph in enumerate(graphs):
    print(indx, min_span_tree(graph))
