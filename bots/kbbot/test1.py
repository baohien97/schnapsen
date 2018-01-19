import kb, sys
from kb import KB, Boolean, Integer, Constant

# Define our symbols
A = Boolean('A')
B = Boolean('B')
C = Boolean('C')
D = Boolean('D')
# Create a new knowledge base
kb = KB()

# Add clauses
kb.add_clause(A, B, C)
kb.add_clause(~A, B)
kb.add_clause(~B, C)
kb.add_clause(B, ~C)

# add a clause that makes kb unsat
kb.add_clause(~C)


# Print all models of the knowledge base
for model in kb.models():
    print model

# Print out whether the KB is satisfiable (if there are no models, it is not satisfiable)
print kb.satisfiable()

# convert to CNF
# ~A -> B = A or B
# B -> A = ~B or A = add_clause(~B, A)
# A -> (C and D) = ~A or (C and D) = (~A or C) and (~A or D) = add_clause(~A, C); add_clause (~A, D)
#
kb2 = KB()
kb2.add_clause(A, B)
kb2.add_clause(~B, A)
kb2.add_clause(~A, C)
kb2.add_clause(~A, D)

for model in kb2.models():
    print model

# Print out whether the KB is satisfiable (if there are no models, it is not satisfiable)
print kb2.satisfiable()