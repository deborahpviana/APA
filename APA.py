g = [[0, 14, 21, 33, 22, 23, 12, 22, 32, 32, 21, 28, 30, 29, 31, 30, 32, 39, 44, 16],
     [14,  0, 12, 19, 12, 24, 12, 19, 21, 27, 7, 19, 16, 21, 33, 17, 31, 27, 31, 19],
     [21, 12,  0, 15, 22, 16, 11,  9, 12, 15, 11, 29, 19,  9, 24, 23, 20, 19, 24, 15],
     [33, 19, 15,  0, 21, 31, 25, 23,  8, 24, 12, 25,  9, 17, 37, 16, 32, 10, 12, 30],
     [22, 12, 22, 21,  0, 36, 24, 30, 26, 37, 12,  7, 13, 30, 44,  9, 42, 31, 33, 30],
     [23, 24, 16, 31, 36,  0, 13,  8, 25, 13, 26, 43, 35, 16,  8, 39,  9, 32, 38,  7],
     [12, 12, 11, 25, 24, 13,  0, 10, 23, 20, 16, 31, 26, 17, 21, 28, 21, 30, 35,  7],
     [22, 19,  9, 23, 30,  8, 10,  0, 18, 10, 19, 37, 28,  9, 15, 32, 12, 24, 30,  9],
     [32, 21, 12,  8, 26, 25, 23, 18,  0, 17, 15, 32, 17, 10, 31, 23, 25,  7, 13, 26],
     [32, 27, 15, 24, 37, 13, 20, 10, 17,  0, 25, 44, 31,  7, 16, 37,  9, 21, 27, 18],
     [21,  7, 11, 12, 12, 26, 16, 19, 15, 25, 0, 19, 10, 18, 34, 13, 31, 21, 24, 22],
     [28, 19, 29, 25,  7, 43, 31, 37, 32, 44, 19,  0, 16, 37, 51, 10, 49, 35, 36, 38],
     [30, 16, 19,  9, 13, 35, 26, 28, 17, 31, 10, 16,  0, 24, 43,  6, 38, 19, 20, 32],
     [29, 21,  9, 17, 30, 16, 17,  9, 10,  7, 18, 37, 24,  0, 21, 30, 15, 16, 22, 18],
     [31, 33, 24, 37, 44,  8, 21, 15, 31, 16, 34, 51, 43, 21,  0, 47,  7, 36, 42, 15],
     [30, 17, 23, 16,  9, 39, 28, 32, 23, 37, 13, 10,  6, 30, 47,  0, 43, 26, 26, 35],
     [32, 31, 20, 32, 42,  9, 21, 12, 25,  9, 31, 49, 38, 15,  7, 43,  0, 30, 36, 16],
     [39, 27, 19, 10, 31, 32, 30, 24,  7, 21, 21, 35, 19, 16, 36, 26, 30,  0,  6, 33],
     [44, 31, 24, 12, 33, 38, 35, 30, 13, 27, 24, 36, 20, 22, 42, 26, 36,  6,  0, 38],
     [16, 19, 15, 30, 30,  7,  7,  9, 26, 18, 22, 38, 32, 18, 15, 35, 16, 33, 38,  0]]
# vertices não visitados
vnv = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

c = [[0, 0],  [1, 19], [2, 30], [3, 16], [4, 23],
     [5, 11], [6, 31], [7, 15], [8, 28], [9, 8],
     [10, 8], [11, 7], [12, 14],[13, 6], [14, 19],
     [15, 11],[16, 26],[17, 17],[18, 6], [19, 15]]

# VIZINHO MAIS PRÓXIMO
rotas = []
tcont = 0
capacidade = 160
# start = True

while True:
    carga_atual = 0
    distancia = 0
    rota = []
    i = 0
    index = 0

    if len(vnv) == 1:
        break

    while ((carga_atual + c[index][1]) <= capacidade):
        menor = 100
        index = 0
        j = 0

        if (not vnv):
            break
        """
        if len(vnv) == 1:
          menor = g[i][0]"""

        rota.append(i)
        print("rotas depois: {}".format(rota))

        carga_atual += c[i][1]
        print("carga atual = {}".format(carga_atual))

        vnv.remove(i)
        print("depois de apagar: {}".format(vnv))

        while j < len(g):  # colocar dentro de uma função
            # print("entrei no for j = {}".format(j))
            if (j in vnv) and (g[i][j] < menor):
                if ((carga_atual + c[j][1]) <= capacidade):  # verifica capacidade aqui
                    menor = g[i][j]
                    index = j
            j += 1

        if (index != 0):
            i = index
            distancia += menor
        else:
            menor = g[i][0]
            break

    distancia += g[i][0]
    rota.append(0)
    print("rota = {}".format)

    tcont += distancia
    rotas.append(rota)
    vnv.insert(0, 0)

print("rotas = {}".format(rotas))
print("rota = {}".format(rota))
print("tcont = {}".format(tcont))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from random import randint

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Fazendo mudanças na vizinhança

a = [0, 6, 19, 5, 7, 2, 13, 9, 16, 0]
print("Rota original a = {}".format(a))
neighborhood = []

def vizinhanca(a):
  for i in range(0, len(a)):
    for j in range(0, len(a)):
      l_aux = a.copy()
      #print('l_aux = {}'.format(l_aux))
      aux = l_aux[i]
      #print('aux = {}'.format(aux))
      if j > i:
        l_aux[i] = l_aux[j]
        l_aux[j] = aux
        neighborhood.append(l_aux)
        #print('l_aux modificado = {}'.format(l_aux))

vizinhanca(a)
#print(neighborhood)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Escolhendo um vizinho aleátorio para o método de descida randomica

new_viz = []
def viz_radom(tam_list):
  while True:  
    viz = randint(0,(tam_list - 1))
    if(viz in new_viz):
      pass
    else:
      new_viz.append(viz)
      #print('new_viz = {}'.format(new_viz))
      return viz

"""for i in range(len(neighborhood)):
  n = viz_radom(len(neighborhood))
  print(new_viz, n)"""

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Calculando a distancia total percorrida na rota

def distancia(a_list):
  cont = 0
  for i in range(0, (len(a_list) - 1)):
    cont += g[a_list[i]][a_list[i + 1]]
    #print(cont)
    
  return cont

# 12 + 7 + 7 + 8 + 9 + 9 + 7 + 9 + 32
#contador = distancia(a)
#print("contador = {}".format(contador))
  
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#METODO DE DESCIDA RANDÔMICA

inter_max = 44
i = 0

while i < inter_max:
  i += 1
  new_v = viz_radom(len(neighborhood))
  print(f"new_v = {new_v}")
  s = a.copy()
  print(f"s = {s}")
  s_ = neighborhood[new_v].copy()
  print(f"s_ = {s_}")
  
  #comparar melhor resultado
  print("comparando as distancias")
  rs  = distancia(s)
  print(f"rs = {rs}")
  rs_ = distancia(s_)
  print(f"rs_ = {rs_}")
  
  if rs_ < rs:
    i = 0
    s = s_
    a = s.copy()
    print(f"novo s = {s}")
    
print('Melhor solução = {}'.format(s))
print(f"nova distancia = {distancia(s)}")
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
