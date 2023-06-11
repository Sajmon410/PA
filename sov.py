import heapq


class Vertex:
    def __init__(self, name=None, parent=None, data=None):
        self.parent = parent
        self.data = data
        self.name = name


class Edge:
    def __init__(self, source=None, destination=None, weight=None):
        self.source = source
        self.destination = destination
        self.weight = weight


class Graph:
    def __init__(self, vertex=None, edge=None):
        self.vertex = vertex
        self.edge = edge

    def __str__(self):
        string = ""
        for edge in self.edge:
            string += (
                "src "
                + str(edge.source.name)
                + " -> dst "
                + str(edge.destination.name)
                + ", w = "
                + str(edge.weight)
                + "\n"
            )
        return string


def ShortestPath(graph, source_vertex, destination_vertex):
    distances = {}
    previous_vertexes = {}

    for vertex in graph.vertex:
        if vertex == source_vertex:
            distances[vertex] = 0
        else:
            distances[vertex] = float("inf")

    priority_queue = [(0, source_vertex)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for edge in graph.edge:
            if edge.source == current_vertex:
                neighbor = edge.destination
                distance = current_distance + edge.weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_vertexes[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor))

    if destination_vertex not in previous_vertexes:
        print("There is no path from", source_vertex, "to", destination_vertex)
        return

    path = []
    current_vertex = destination_vertex
    while current_vertex != source_vertex:
        path.insert(0, current_vertex.name)
        current_vertex = previous_vertexes[current_vertex]
    path.insert(0, source_vertex.name)

    print("Shortest path:", path)
    print("Length:", distances[destination_vertex])


a = Vertex("A")
b = Vertex("B")
c = Vertex("C")
d = Vertex("D")
e = Vertex("E")
f = Vertex("F")

ab = Edge(a, b, -6)
ad = Edge(a, d, -4)
ae = Edge(a, e, 15)
bc = Edge(b, c, 7)
cf = Edge(c, f, -3)
de = Edge(d, e, 11)
ec = Edge(e, c, 13)
fe = Edge(f, e, 5)

graph = Graph([a, b, c, d, e, f], [ab, ad, ae, bc, cf, de, ec, fe])

print(graph)

ShortestPath(graph, b, f)
