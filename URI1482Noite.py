import networkx as nx

LIMIT = 420

nodes = input()

while (nodes!=0):
  G = nx.Graph() 
  limits =  list(map(int, input().split()))

  outoftime = 0

  for x in range (limits):
    if (limits[x] > LIMIT):
      outoftime += 1 # if for

  """
  for y in range (nodes):
    weight1, weight2 = map(int, input().split())
    weight = max (weight1, weight2)
    G.add_edge(y,y+1, weight)  #end for
  """
  """  
  if (outoftime == 0):
   time = dijkstra_path_length(G, source, target, weight='weight')
   time +=  G.edges(data=True)
   if ( time > limits[node])

  """
  """
  budget = LIMIT
  aux = timemuseum1 + weightedge
  budget = aux - budget
  if(budget < timemuseum2)

  """


"""  
A estrategia é somar o tempo necessario para visita do primeiro museu com o tempo necessario para visitar o proximo museu subtrair o resultado com o limite dado 420 minutos(7 horas) e obter um novo orçamento e refazer as operações anteriores se for possivel

"""