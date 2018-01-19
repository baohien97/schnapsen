import kb, sys
from kb import KB, Boolean, Integer, Constant

# Define our propositional symbols
# J1 is true if the card with index 1 is a jack, etc
# You need to initialise all variables that you need for you strategies and game knowledge.
# Add those variables here.. The following list is complete for the Play Jack strategy.

CA = Boolean('ca')
C10 = Boolean('c10')
CK = Boolean('ck')
CQ = Boolean('cq')
CJ = Boolean('cj')
DA = Boolean('da')
D10 = Boolean('d10')
DK = Boolean('dk')
DQ = Boolean('dq')
DJ = Boolean('dj')
HA = Boolean('ha')
H10 = Boolean('h10')
HK = Boolean('hk')
HQ = Boolean('hq')
HJ = Boolean('hj')
SA = Boolean('sa')
S10 = Boolean('s10')
SK = Boolean('sk')
SQ = Boolean('sq')
SJ = Boolean('sj')

PCA = Boolean('PCA')
PCK = Boolean('PCK')
PCQ = Boolean('PCQ')
PCJ = Boolean('PCJ')
PC10 = Boolean('PC10')
PDA = Boolean('PDA')
PDK = Boolean('PDK')
PDQ = Boolean('PDQ')
PDJ = Boolean('PDJ')
PD10 = Boolean('PD10')
PHA = Boolean('PHA')
PHK = Boolean('PHK')
PHQ = Boolean('PHQ')
PHJ = Boolean('PHJ')
PH10 = Boolean('PH10')
PSA = Boolean('PSA')
PS10 = Boolean('PS10')
PSK = Boolean('PSK')
PSQ = Boolean('PSQ')
PSJ = Boolean('PSJ')

# Create a new knowledge base
kb = KB()

# GENERAL INFORMATION ABOUT THE CARDS
kb.add_clause(CQ)
kb.add_clause(CK)
kb.add_clause(DQ)
kb.add_clause(DK)
kb.add_clause(HQ)
kb.add_clause(HK)
kb.add_clause(SQ)
kb.add_clause(SK)


# DEFINITION OF THE STRATEGY
# Add clauses (This list is sufficient for this strategy)
# PJ is the strategy to play jacks first, so all we need to model is all x PJ(x) <-> J(x),
# In other words that the PJ strategy should play a card when it is a jack
# Add here other strategies

kb.add_clause((~CQ, ~CK),(CQ, CK)) and

kb.add_clause(CQ)
# Print all models of the knowledge base
for model in kb.models():
    print model

# Print out whether the KB is satisfiable (if there are no models, it is not satisfiable)
print kb.satisfiable()
