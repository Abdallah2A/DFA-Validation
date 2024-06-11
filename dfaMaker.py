# First we need to take DFA 5-tuple from user
# Q is a fnite set called the states
while True:
    try:
        x = int(input("Enter number of states: "))
        Q = [input("Enter state "+str(i+1)+ ": ") for i in range(0,x)]
        break
    except ValueError as err:
        print("Error: ",err)

# Σ is a fnite set called the alphabet
while True:
    try:
        y = int(input("Enter number of alphabets: "))
        E = [input("Enter alphabet "+str(i+1) +": ") for i in range(0,y)]
        break
    except ValueError as err:
        print("Error: ",err)

# F ⊆ Q is the set of accept states
while True: 
    F = input("Specify the final state: ")
    if not F:
        raise ValueError('empty string')
    if F in Q:
        break
    else:
        print("Final state not in States, Enter valid state from "+str(Q))

K = [0 for i in range(len(Q))]

# δ : Q * Σ -> Q is the transition function
for i in range(len(Q)):
    K[i] = [0 for j in range(len(E))]
    for j in range(len(E)):
        while True:
            try:
                K[i][j]=input("from "+Q[i]+" if "+E[j]+" go: ")
                if not K[i][j]:
                    raise ValueError('empty string')
                if K[i][j] in Q:
                    break
                else:
                    print("State not in States, Enter valid state from "+str(Q))
            except ValueError as err:
                print("Error: ", err)


# Second we need to make function to check the input string from user 
def spot(q, w):
    lis.append(K[Q.index(q)][E.index(w)])
    return K[Q.index(q)][E.index(w)]


# Third we need to take string from the user and check it
while True:
    lis = []
    st=Q[0]
    while True:
        try:
            s = input("Enter String to check: ")
            if not s:
                raise ValueError('empty string')
            break
        except ValueError as err:
            print("Error: ", err, "(alphabets)")
    for i in s:
        st = spot(st, i)
    
# Fourth we need to tell to user if accepted or rejected
    if lis[-1] == F:
        print("ACCEPTED \n"+Q[0]+" --> "+" --> ".join(lis))
    else :
        print("REJECTED \n"+Q[0]+" --> "+" --> ".join(lis))