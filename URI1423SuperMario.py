import networkx as nx

trials = int(input(""))  # numbers of trials
str = input("")

while trials > 0: 

    a, b, m, l, k = str.split(" ")

    a = int(a)
    b = int(b)
    m = int(m)
    l = int(l)
    k = int(k)

    """
    Generation and populating the graph
    """

    G = nx.Graph()

    # village -> role = 1
    # castle -> role = 0
    for i in range(1, (a + 1)):

        G.add_node(i, role = 1)

    for i in range(a + 1, (a + b + 1)):

        G.add_node(i, role = 0)


    for i in range(0, m):

        str = input("")
        a, b, w = str.split(" ")
        a = int(a)
        b = int(b)
        w = int(w)

        G.add_edge(a, b, weight = w)
        

    g = nx.minimum_spanning_tree(G, weight = 'weight', algorithm = 'prim')# generation the minimun spanning tree

    total = 0
    values = []
    weights = [0]
    
    """
    fetching the weights
    """
    for(u ,v ,wt) in g.edges.data('weight'):

        total += wt
        weights.append(wt)

    for i in range(1, len(weights)):
        trim = 0 + weights[i]
        c = False

        for j in range(i + 1, len(weights)):

            if(trim + weights[j]) < l:
                trim += weights[j]
                if j == len(weights) - 1:
                    values.append(trim)
            else:
                values.append(trim)
                break

    for i in range(0, k):
        maxweight = max(values)
        total -= maxweight
        values.remove(maxweight)

    print(total)

    trials -= 1
