from copy import deepcopy


def euler( G ):
    n = len(G)
    result = [0]
    
    def DFS(i):
        for j in range(n):
            if G[i][j] == 1:
                G[i][j] = 2
                G[j][i] = 2
                DFS(j)
                result.append(i)
    
    DFS(0)
    
    for i in range(n):
        for j in range(n):
            if G[i][j] == 2:
                G[i][j] = 1

    return result
  
  
### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik
  
  
G = [[0,1,1,0,0,0],
     [1,0,1,1,0,1],
     [1,1,0,0,1,1],
     [0,1,0,0,0,1],
     [0,0,1,0,0,1],
     [0,1,1,1,1,0]]


GG = deepcopy( G )
cycle = euler( G )

if cycle == None: 
  print("Błąd (1)!")
  exit(0)
  
u = cycle[0]
for v in cycle[1:]:
  if GG[u][v] == False:
    print("Błąd (2)!")
    exit(0)
  GG[u][v] = False
  GG[v][u] = False
  u = v
  
for i in range(len(GG)):
  for j in range(len(GG)):
    if GG[i][j] == True:
      print("Błąd (3)!")
      exit(0)
      
print("OK")
GG = deepcopy( G )
cycle = euler( G )

if cycle == None: 
  print("Błąd (1)!")
  exit(0)
  
u = cycle[0]
for v in cycle[1:]:
  if GG[u][v] == False:
    print("Błąd (2)!")
    exit(0)
  GG[u][v] = False
  GG[v][u] = False
  u = v
  
for i in range(len(GG)):
  for j in range(len(GG)):
    if GG[i][j] == True:
      print("Błąd (3)!")
      exit(0)
      
print("OK")