from kb import KB, Boolean, Integer

# Initialise all variables that you need for you strategies and game knowledge.
# Add those variables here.. The following list is complete for the Play Jack strategy.
J0 = Boolean('j0')
J1 = Boolean('j1')
J2 = Boolean('j2')
J3 = Boolean('j3')
J4 = Boolean('j4')
J5 = Boolean('j5')
J6 = Boolean('j6')
J7 = Boolean('j7')
J8 = Boolean('j8')
J9 = Boolean('j9')
J10 = Boolean('j10')
J11 = Boolean('j11')
J12 = Boolean('j12')
J13 = Boolean('j13')
J14 = Boolean('j14')
J15 = Boolean('j15')
J16 = Boolean('j16')
J17 = Boolean('j17')
J18 = Boolean('j18')
J19 = Boolean('j19')
PJ0 = Boolean('pj0')
PJ1 = Boolean('pj1')
PJ2 = Boolean('pj2')
PJ3 = Boolean('pj3')
PJ4 = Boolean('pj4')
PJ5 = Boolean('pj5')
PJ6 = Boolean('pj6')
PJ7 = Boolean('pj7')
PJ8 = Boolean('pj8')
PJ9 = Boolean('pj9')
PJ10 = Boolean('pj10')
PJ11 = Boolean('pj11')
PJ12 = Boolean('pj12')
PJ13 = Boolean('pj13')
PJ14 = Boolean('pj14')
PJ15 = Boolean('pj15')
PJ16 = Boolean('pj16')
PJ17 = Boolean('pj17')
PJ18 = Boolean('pj18')
PJ19 = Boolean('pj19')

def general_information(kb):
    # GENERAL INFORMATION ABOUT THE CARDS
    # This adds information which cards are Jacks
    # Add here whatever is needed for your strategy.
    #Jacks
    kb.add_clause(J4)   #cloves
    kb.add_clause(J9)   #diamomds
    kb.add_clause(J14)  #hearts
    kb.add_clause(J19)  #spades

    #Queens
    kb.add_clause(J3)   #cloves
    kb.add_clause(J8)   #diamonds
    kb.add_clause(J13)  #hearts
    kb.add_clause(J18)  #spades
    
    #Kings
    kb.add_clause(J2)   #cloves
    kb.add_clause(J7)   #diamonds
    kb.add_clause(J12)  #hearts
    kb.add_clause(J17)  #spades

def strategy_knowledge(kb):
    #CHEAP CARD STRATEGY
    # Cheap card strategy is the strategy to play cheap cards first (Jacks, Kings, Queens),
    # all x PJ(x) <-> J(x) (for every cheap card in had, play that card)

    # Jacks
    kb.add_clause(~J4, PJ4)
    kb.add_clause(~J9, PJ9)
    kb.add_clause(~J14, PJ14)
    kb.add_clause(~J19, PJ19)
    kb.add_clause(~PJ4, J4)
    kb.add_clause(~PJ9, J9)
    kb.add_clause(~PJ14, J14)
    kb.add_clause(~PJ19, J19)

    #Queens
    kb.add_clause(~J3, PJ3)
    kb.add_clause(~J8, PJ8)
    kb.add_clause(~J13, PJ13)
    kb.add_clause(~J18, PJ18)
    kb.add_clause(~PJ3, J3)
    kb.add_clause(~PJ8, J8)
    kb.add_clause(~PJ13, J13)
    kb.add_clause(~PJ18, J18)

    #Kings
    kb.add_clause(~J2, PJ2)
    kb.add_clause(~J7, PJ7)
    kb.add_clause(~J12, PJ12)
    kb.add_clause(~J17, PJ17)
    kb.add_clause(~PJ2, J2)
    kb.add_clause(~PJ7, J7)
    kb.add_clause(~PJ12, J12)
    kb.add_clause(~PJ17, J17)



def strategy_marriages(kb):
    #MARRIAGE STRATEGY

    # Marriage Cloves
    kb.add_clause(~J2, ~J3, PJ2, PJ3)
    kb.add_clause(J2, ~PJ2)
    kb.add_clause(J3, ~PJ2)
    kb.add_clause(J2, ~PJ3)
    kb.add_clause(J3, ~PJ3)

    # Marriage Diamonds
    kb.add_clause(~J7, ~J8, PJ7, PJ8)
    kb.add_clause(J7, ~PJ7)
    kb.add_clause(J8, ~PJ7)
    kb.add_clause(J7, ~PJ8)
    kb.add_clause(J8, ~PJ8)

    # Marriage Hearts
    kb.add_clause(~J12, ~J13, PJ12, PJ13)
    kb.add_clause(J12, ~PJ12)
    kb.add_clause(J13, ~PJ12)
    kb.add_clause(J12, ~PJ13)
    kb.add_clause(J13, ~PJ13)

    # Marriage Spades
    kb.add_clause(~J17, ~J18, PJ17, PJ18)
    kb.add_clause(J17, ~PJ17)
    kb.add_clause(J18, ~PJ17)
    kb.add_clause(J17, ~PJ18)
    kb.add_clause(J18, ~PJ18)
