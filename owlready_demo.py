from owlready2 import *
onto = get_ontology("water.owl")
print(list(onto.individuals()))
