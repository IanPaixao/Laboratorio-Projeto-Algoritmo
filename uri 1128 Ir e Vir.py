import networkx as nx

error = 0
nodes, edges = map(int, input().split())

while (nodes!=0 and edges !=0): 

  G = nx.DiGraph()

  for x in range(nodes):
    G.add_node(x+1) #end for

  for x in range(edges):
    numbers = input().split()
    
    if numbers[2] == 1:
      G.add_edge(numbers[0],numbers[1]) #end if

    else:
    #if numbers[2] == 2:  
      G.add_edge(numbers[0],numbers[1])
      G.add_edge(numbers[1],numbers[0]) #end else end for

  for x in range (nodes):
    for y in range(nodes):
      if x != y:
        if G.has_edge(x, y) == False:
          error += 1 #end if end for
  
  if error == 0:
    print(1) #end if
  else:
    print(0) #end else
  
  nodes, edges = map(int, input().split()) #end while


# A ideia é verificar a existencia de arestas entre os vertices
# no intuito de provar a conectividade