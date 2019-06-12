  import networkx as nx

  cards = int(input())
  G = nx.Graph()
  numbers = input()
  numbers = numbers.split()

  """
  Creating and populating the graph
  """

  #Creating nodes with values with attributes
  for i in range(len(numbers)):
    G.add_node(i,value = int(numbers[i]) - 1)
  #Creating edges with weight equal to 1
  for x in range ((cards- 1)):
    edges = input()
    node1,node2 = edges.split(" ")
    node1 = int(node1)
    node2 = int(node2)
    G.add_edge(node1 - 1,node2 - 1, weight = 1)  
  
  
  NodeAttr = nx.get_node_attributes(G,'value')

  array = []
  
  """
  Sorting the array and iterantig it searching for the maxinum number of points 
  """
  #Sorting
  for i in range(int(cards/2)):
    for j in range(cards):
      if(NodeAttr[j] == i):
        array.append(j)
    pass
  pass
  weight = 0
  # Searching for points
  for i in range(0,len(array),2):
    weight = weight + nx.shortest_path_length(G,array[i],array[i+1])
  pass
  print(weight)
