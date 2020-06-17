from collections import defaultdict

neg = '~'
# directed graph class
#  adapted from:
#  src: https://www.geeksforgeeks.org/generate-graph-using-dictionary-python/
class dir_graph:
    def __init__(self):
        # create an empty directed graph, represented by a dictionary
        #  The dictionary consists of keys and corresponding lists
        #  Key = node u , List = nodes, v, such that (u,v) is an edge
        self.graph = defaultdict(list)

    # Function that adds an edge (u,v) to the graph
    #  It finds the dictionary entry for node u and appends node v to its list
    # performance: O(1)
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Function that outputs the edges of all nodes in the graph
    #  prints all (u,v) in the set of edges of the graoh
    # performance: O(m+n) m = #edges , n = #nodes
    def print(self):
        edges = []
        # for each node in graph
        for node in self.graph:
            # for each neighbour node of a single node
            for neighbour in self.graph[node]:
                # if edge exists then append
                edges.append((node, neighbour))
        return edges


# 2-CNF class
#  Class storing a boolean formula in Conjunctive Normal Form of literals
#  where the size of clauses is at most 2
#  -NOTATION-
#    The CNF is represented as a list of lists
#    e.g [[x, y], [k, z]] == (x or y) and (k or z)
#    i.e Conjunction of inner lists , where the inner lists are disjunctions
#    of literals
#    Negation is represented with ~ .  ~x == negation of literal x
# class two_cnf:
class two_cnf:
    def __init__(self):
        self.con = []

    # adds a clause to the CNF
    # performance O(1)
    def add_clause(self, clause):
        if len(clause) <= 2:
            self.con.append(clause)
        else:
            print("error: clause contains > 2 literals")

    # returns a set of all the variables in the CNF formula
    def get_variables(self):
        vars = set()
        for clause in self.con:
            for literal in clause:
                vars.add(literal)
        return vars

    def print(self):
        print(self.con)


# helper function that applies the double negation rule to a formula
#   the function removes all occurrences ~~ from the formula
def double_neg(formula):
    return formula.replace((neg+neg), '')


def two_sat_solver(two_cnf_formula):
    # setup the edges of the graph
    # G = (V,E) , V = L U ~L where L = set of variables in 2-CNF
    # E =
    # {(~u,v),(~v,u) | for all clauses [u,v] } U {(~u,u) | for all clauses [u]}
    graph = dir_graph()
    for clause in two_cnf_formula.con:
        if len(clause) == 2:
            u = clause[0]
            v = clause[1]
            graph.addEdge(double_neg(neg+u), v)
            graph.addEdge(double_neg(neg+v), u)
        else:
            graph.addEdge(double_neg(neg+clause[0]), clause[0])
    print(graph.print())


# ======= 2-CNF setup =======
formula = two_cnf()
formula.add_clause(['x', 'y'])
formula.add_clause(['y', '~z'])
two_sat_solver(formula)
