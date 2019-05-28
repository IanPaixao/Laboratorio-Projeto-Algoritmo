
def main():
  
  casos = int(input())
  
  for i in range(casos):
    presentes = []
    qntTipos = int(input())
    for j in range(qntTipos):
      aux = input().split(' ')
      aux = list(map(int, aux))
      #qntPresentes 
      #peso
      presentes.append({"q" : aux[0],"peso" : aux[1]})

    melhorPeso = 0
    melhorSobra = 0
    melhorQBrinquedos = 0

    #Existem 2ˆqntTipos de combinacoes de itens
    for x in range(pow(2,qntTipos)):
      
      peso = 0
      qntBrinquedos = 0
      sobra = 0

      for y in range(qntTipos):
        #Utilizamos os bits de para saber a configuracao de opcoes de presentes
        if ((x >> y) % 2) != 0:
          qntBrinquedos = qntBrinquedos + presentes[y]["q"]
          peso = peso + presentes[y]["peso"]
        else:
          sobra = sobra + 1

      if qntBrinquedos > melhorQBrinquedos and peso <= 50:
        melhorPeso = peso
        melhorSobra = sobra
        melhorQBrinquedos = qntBrinquedos
    print()    
    print(melhorQBrinquedos," brinquedos")  
    print("Peso ",melhorPeso," kg")  
    print("sobram(m) ", sobra," pacotes(s)")
main()    



