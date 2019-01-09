with open("state.txt",'r') as f:
    data = f.readlines()
    codesFile = open('state-codes.txt','w')
    namesFile = open('state-names.txt','w')
    c = 0
    for l in data:
        c+=1
        state = l.split("-")
        name = state[0].strip()
        code = state[1].strip()
        codesFile.write("'"+code.lower()+"'"+",")
        namesFile.write(name+"\n")
    codesFile.close()
    namesFile.close()
    print(c)




    