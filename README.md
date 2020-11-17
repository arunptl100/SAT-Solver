# 2-SAT-Solver
A linear time 2-SAT solver in python.

The solver is based on the fact that the disjunction (u v x) can be re-written as (~u -> v) or (~v -> u).
Given a 2-CNF boolean formula, the solver constructs a graph G=(V,E) based on the above fact. Where:
  - V = V u ~V
    - i.e V = set of variables in the CNF and their negation
  - E = {(~u, v),(~v,u) | for all clauses [u,v] } U {(~u,u) | for all clauses [u]}

G has 2|V| nodes and 2m edges where m is the number of literals in the CNF
Next the solver computes the strongly connected components of G using Kosaraju’s algorithm
in O(|V|+|E|) time.
If there exists a variable x such that x ~> ~x ~> x occurs in a strongly connected component , then the solver returns False, signifying that the formula is unsatisfiable. It returns True otherwise, showing that the formula is satisfiable. 

Key: 
 - u = union 
 - v = logical disjunction (or)
 - ~ = logical negation (not) 
 - -> = logical implication 

## User guide
 Clone the repository.
 To add a 2-CNF formula, open `sat-solver.py` and modify the lines from `169` onwards.
 To add the clause (u V ~x) to the formula, add the line `formula.add_clause(['u', '~x'])`.
 Run the solver using `python3` 
  - `python sat-solver.py` from the command line 

