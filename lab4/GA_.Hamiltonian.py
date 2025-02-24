from itertools import permutations
import networkx as nx

def overlap(a, b):
    """Returns the maximum overlap between two strings."""
    max_overlap = 0
    for i in range(1, min(len(a), len(b)) + 1):
        if a[-i:] == b[:i]:
            max_overlap = i
    return max_overlap

def build_graph(sequences):
    """Constructs a directed graph based on maximum overlap."""
    G = nx.DiGraph()
    for seq in sequences:
        G.add_node(seq)
    
    for a in sequences:
        for b in sequences:
            if a != b:
                ov = overlap(a, b)
                if ov > 0:
                    G.add_edge(a, b, weight=-ov) 
    return G

def find_hamiltonian_path(G):
    """Finds a Hamiltonian Path in the graph."""
    for perm in permutations(G.nodes()):
        valid = True
        for i in range(len(perm) - 1):
            if not G.has_edge(perm[i], perm[i + 1]):
                valid = False
                break
        if valid:
            return perm
    return None

def assemble_genome(sequences):
    """Assembles the genome from given sequences using Hamiltonian Path approach."""
    G = build_graph(sequences)
    path = find_hamiltonian_path(G)
    if path is None:
        return "No Hamiltonian Path found"
    
    genome = path[0]
    for i in range(1, len(path)):
        ov = overlap(genome, path[i])
        genome += path[i][ov:]
    
    return genome

sequences = ["ATG", "TGC", "GCA", "CAA", "AAA", "AAG", "AGC", "CCT", "CTA", "TAG", "GCG", "GCC", "CCG"]
assembled_genome = assemble_genome(sequences)
print("Assembled Genome:", assembled_genome)