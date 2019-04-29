import networkx as nx


  str = input()
  nodes, edges = str.split(" ")
  nodes = int(nodes) 
  edges = int(edges) 
  while(nodes and edges > 0): 

    G = nx.Graph() 

    """
    Generating and populating the graph
    """
    for i in range(0, m):
        str = input()
        source, destiny, weight = str.split(" ")
        source = int(source)
        destiny = int(destiny)
        weight = int(weight)
        G.add_edge(source,destiny, weight=weight)
  
    """
    Extracting the minimum spanning
    """
    MST=nx.minimum_spanning_tree(G)

    weightG = 0
    weightMST = 0

    """
    Extracting the sum of the weight from the graph and the minimum spanning
    """
  
    for i,j,w in G.edges.data('weight'):
      weightG += w

    for i,j,w in MST.edges.data('weight'):
      weightMST += w

    result = weightG - weightMST

    print(result)
    str = input()
    nodes, edges = str.split(" ")
    nodes = int(nodes)
    edges = int(edges)
