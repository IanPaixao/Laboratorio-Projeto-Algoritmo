import networkx as nx

  firstline = input("")
  h = 1
  while(firstline != '0 0'):
    """
    Generating and populating the graph
    """
    G = nx.Graph() #generating the graph
    nodes,edges = linha1.split(" ")
    nodes = int(nodes) #nodes
    edges = int(edges) #edges
    while(times > 0):
      secondline = input("")
      source,destination,source = secondline.split(" ")
      source = int(source) #origin
      destination = int(destination) # destination
      weights = int(weights) # weight of the edge
      G.add_edge(source,destination,weight=weights)# adding edge
      times = times - 1


    avg = nx.minimum_spanning_tree(G)#minimum spanning tree 
    
    
    trials = input()
    trials = int(trials)
    print("Instancia",h)
    
    """
    search for the heaviest weight between source and destination
    """
    while(trials > 0):
      secondline = input("")
      source2,destination2 = secondline.split(" ")
      source2 = int(source2) #origem
      destination2 = int(destination2) #destino

      #search for the shorteste path between source2 and destination2
      path = nx.shortest_path(avg,source = source2,target = destination2)
      greater = 0
      size = len(path)
      
      """
      compares two vertices of the path between source and target two times the weight of each edge
      """
      for i in range(0,(size-1)):
        weight = avg[int(path[i])][int(path[i+1])]['weight']
        if weight > greater:
          greater = weight    
      print(greater)   
      trials = trials - 1 
    h = h + 1       
    firstline = input("")       
