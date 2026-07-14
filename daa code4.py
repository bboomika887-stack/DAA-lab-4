import streamlit as st
import heapq

st.set_page_config(page_title="Dijkstra's Algorithm", layout="centered")

st.title("🚀 Dijkstra's Shortest Path Algorithm")

# ---------------- Dijkstra ----------------

def dijkstra(graph, source):

    n = len(graph)

    dist = [float("inf")] * n
    prev = [None] * n

    dist[source] = 0

    pq = [(0, source)]
    visited = set()

    while pq:
        d, u = heapq.heappop(pq)

        if u in visited:
            continue

        visited.add(u)

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))

    return dist, prev


def reconstruct_path(prev, source, target):

    path = []
    node = target

    while node is not None:
        path.append(node)
        node = prev[node]

    path.reverse()

    if path and path[0] == source:
        return path

    return []

# ---------------- Graph ----------------

graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: [(4, 3)],
    4: [(5, 2)],
    5: []
}

source = st.number_input(
    "Enter Source Vertex",
    min_value=0,
    max_value=len(graph)-1,
    value=0,
    step=1
)

if st.button("Find Shortest Paths"):

    dist, prev = dijkstra(graph, source)

    st.subheader(f"Shortest Paths from Vertex {source}")

    data = []

    for v in range(len(graph)):

        path = reconstruct_path(prev, source, v)

        if path:
            path_str = " → ".join(map(str, path))
        else:
            path_str = "No Path"

        if dist[v] == float("inf"):
            distance = "∞"
        else:
            distance = dist[v]

        data.append({
            "Vertex": v,
            "Distance": distance,
            "Path": path_str
        })

    st.table(data)
