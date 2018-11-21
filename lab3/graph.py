# python 3 only!!!
import collections
import math
from itertools import islice


class Graph:

    def __init__(self):
        self.vertices = set()
        # makes the default value for all vertices an empty list
        self.edges = collections.defaultdict(list)
        self.weights = {}

    def add_vertex(self, value):
        self.vertices.add(value)

    def add_edge(self, from_vertex, to_vertex, distance):
        if from_vertex == to_vertex:
            pass  # no cycles allowed
        self.edges[from_vertex].append(to_vertex)
        self.weights[(from_vertex, to_vertex)] = distance

    def __str__(self):
        string = "Vertices: " + str(self.vertices) + "\n"
        string += "Edges: " + str(self.edges) + "\n"
        string += "Weights: " + str(self.weights)
        return string


def dijkstra(graph, start):
    S = set()

    delta = dict.fromkeys(list(graph.vertices), math.inf)

    delta[start] = 0

    while S != graph.vertices:
        v = min((set(delta.keys()) - S), key=delta.get)

        for neighbor in set(graph.edges[v]) - S:
            new_path = delta[v] + graph.weights[v, neighbor]

            if new_path < delta[neighbor]:
                delta[neighbor] = new_path

        S.add(v)

    return delta


idx_of_clients = []


def read_graph_from_file(file_in):
    graph = Graph()
    lines = open(file_in).readlines()

    # reading first line
    first_line = lines[0]
    first_line_val = first_line.split(' ')

    num_of_vertx = int(first_line_val[0])
    for i in range(1, num_of_vertx + 1):
        graph.add_vertex(i)
    num_of_edges = int(first_line_val[1])

    # reading second line
    second_line = lines[1]
    idx_of_clients.extend([int(x) for x in second_line.split()])

    # reading least lines
    with open(file_in) as f:
        for line in islice(f, 2, num_of_edges + 2):
            values = [int(x) for x in line.split()]
            graph.add_edge(values[0], values[1], values[2])
            graph.add_edge(values[1], values[0], values[2])
    return graph


def max_in_list(list_in):
    j = 0
    for i in list_in:
        if i > j:
            j = i
        else:
            pass
    return j


def min_in_list(list_in):
    j = 10 ** 10
    for i in list_in:
        if i == 0:
            pass
        elif i < j:
            j = i
        else:
            pass
    return j


def write_into_file(the_file, text):
    with open(the_file, 'a') as the_file:
        the_file.write(text)


def find_min_max_latency_time(graph):
    list_of_maxes = []
    for i in range(1, graph.vertices.__len__() + 1):
        if i in idx_of_clients:
            pass
        else:
            latencies = list(dijkstra(graph, i).values())
            max_latency_time = max_in_list(latencies)
            list_of_maxes.append(max_latency_time)
    return min_in_list(list_of_maxes)


if __name__ == '__main__':
    G = Graph()
    G = read_graph_from_file('gamesrv.in')
    result = find_min_max_latency_time(G)
    write_into_file('gamesrv.out', str(result))
