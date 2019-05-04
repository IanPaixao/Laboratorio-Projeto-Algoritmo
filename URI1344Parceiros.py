import networkx as nx

"""
Method to remove nodes lesses than the established K variable form the graph
"""
def rmvNode(G,degree):
  aux = True
  while(aux):
    G1 = G.copy()
    aux = False
    for x in G1.nodes():
      if (degree > G.degree(x)):
        G.remove_node(x)
        aux = True
pass

def main():
  inputs = input()
  while(inputs != '0 0 0'):   
    G = nx.Graph()
    nodes,edges,degree = inputs.split()
    nodes = int(nodes)
    edges = int(edges)
    degree = int(degree)

    """
    Generating and populating the graph
    """

    while edges > 0:
      connection = input()
      node1,node2 = connection.split()
      G.add_edge(int(node1),int(node2))
      edges = edges - 1
    connection = input()

    rmvNode(G,degree)
    size = len(G)
  
    """
    Extrating the connected subgraphs
    """

    if(size > 0):
      connected = max(nx.connected_component_subgraphs(G), key = len)
      print(len(connected))
    else:
      print("0")

main()    
