from collections import defaultdict, deque

def build_de_bruijn_graph(kmers):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)

    for kmer in kmers:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        graph[prefix].append(suffix)
        out_degree[prefix] += 1
        in_degree[suffix] += 1
    
    return graph, in_degree, out_degree


def find_start_node(graph, in_degree, out_degree):
    start = None
    for node in graph:
          if out_degree[node] > in_degree[node]:
            return node
    return list(graph.keys())[0]


def eulerian_path(graph, start):
    path = []
    stack = [start]
    
    while stack:
        node = stack[-1]
        if graph[node]:
            next_node = graph[node].pop()
            stack.append(next_node)
        else:
            path.append(stack.pop())
    
    path.reverse()
    return path


def reconstruct_string_from_kmers(kmers):
    graph, in_degree, out_degree = build_de_bruijn_graph(kmers)
    start_node = find_start_node(graph, in_degree, out_degree)
    path = eulerian_path(graph, start_node)
    
    reconstructed_string = path[0]
    for node in path[1:]:
        reconstructed_string += node[-1]
    
    return reconstructed_string


kmers = ["ATG", "TGC", "GCA", "CAT", "ATC", "TCA", "CAG", "AGT", "GTT", "TTA", "TAC", "ACT"]
reconstructed_string = reconstruct_string_from_kmers(kmers)
print("Reconstructed string:", reconstructed_string)