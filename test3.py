def do(name,alpha,num):
    return f"""
        <!-- http://ssei.herokuapp.com/water#{name} -->

    <owl:NamedIndividual rdf:about="http://ssei.herokuapp.com/water#{name}">
        <rdf:type rdf:resource="http://ssei.herokuapp.com/water#State"/>
        <ontologies:alpha_state_code rdf:datatype="http://www.w3.org/2001/XMLSchema#string">{alpha}</ontologies:alpha_state_code>
        <ontologies:name rdf:datatype="http://www.w3.org/2001/XMLSchema#string">{name}</ontologies:name>
        <ontologies:numeric_state_code rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">{num}</ontologies:numeric_state_code>
    </owl:NamedIndividual>

    """

f = open('all.txt','r').readlines()
f2 = open('all2.txt','w')

for state in f:
    name = ''
    if state[1].isdigit():
        name = state[0]
        code = state[1]
        alpha = state[2]
    else:
        name = state[0]+"_"+state[1]
        code = state[2]
        alpha = state[3]
    f2.write(do(name,alpha,code))
f2.close()
