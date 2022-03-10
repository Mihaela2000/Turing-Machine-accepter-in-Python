#Buzdugan Mihaela

#functia care citeste codificarea unei Masini Turing 
def readTM(codifMT):
  b = codifMT.split("\n")
  name_ex = b[0]
  cuvinte = b[1]
  nr_stari = int(b[2])
  ultima_stare = nr_stari - 1

  nr_tranz = len(b) - 4
  
  tranz = b.copy()
  if tranz[-1] == '':
    tranz.pop(-1)
    nr_tranz -=1
  tranz.pop(3)
  tranz.pop(2)
  tranz.pop(1)
  tranz.pop(0)

  stari_finale = b[3].split()
  F = list(stari_finale)

  T = (name_ex, cuvinte, ultima_stare, tranz, F, nr_tranz)
  return (T)

#functie care converteste o lista intr-un string
def listToString(s):
  st = " "
  return (st.join(s))

#functia step primeste un cuvant, starea actuala si tranzatiile masinii
# aceasta returneaza un pas facaut pe un cuvant
def step(u, q, v, T, nr_tranz):
  i = 0
  f = 'False'

  while nr_tranz:
    if q == T[i][0]:
      if v[0] == T[i][2]:
        q_new = T[i][4]
        if T[i][8] == 'R':
          u_new = u + T[i][6]
          v_new = v[1:]
          if v_new == '':
            v_new = '#'
        if T[i][8] == 'L':
          u_new = u[:-1]
          v_new = u[-1] + T[i][6] + v[1:]
          if u_new == '':
            u_new = '#'
        if T[i][8] == 'H':
          u_new = u
          v_new = T[i][6] + v[1:]
        return(u_new, q_new, v_new)
    i +=1
    nr_tranz -=1
  
  return (f)

#functia accept primeste configuratia unei masini si un cuvant
# aceasta returneaza True daca masina accepta sau False in caz contrar
def accept( F, T, nr_tranz, cuv):
  q = 0
  i = 0
  j = 0
  nr_tranz_fix = nr_tranz
  boolean =[]
  #parcurgem fiecare tranzitie pana gasim starea actuala a cuvantului
  # si caracterul unde indica aceasta
  while nr_tranz:  
    if int(T[i][0]) == q:
      if cuv[j] == T[i][2]:
        #schimb caracterul indicat cu noul caracter pe care il gasesc in tranzitie
        cuv =cuv[:j] + T[i][6] + cuv[j+1:]
        #mut pozitia starii actuale la L/R/H
        # daca am iesit din cuvant , adaug # pe pozitia indicata 
        if T[i][8] == 'L':
          j -=1
          if j < 0:
            cuv = '#' + cuv[:]

        if T[i][8] == 'R':
          j +=1
          if j > len(cuv) - 1:
            cuv = cuv[:] + '#'
        
        #actualizez starea actuala cu starea pe care am gasit-o pe tranzitie
        q = int(T[i][4])
       
        if F[0] != '-':
          if T[i][8] == 'H':
            boolean = 'True'
            return (boolean)
        
          if q == int(listToString(F[0])):
            boolean = 'True'
            return (boolean)
        i = -1

    i +=1  
    if i+1 > nr_tranz_fix:
      i -=1
      
      boolean = 'False'
      return (boolean)
    
#functia k_accept face acelasi lucru ca si functia accept, dar in k pasi
def k_accept(k, F, T, nr_tranz, cuv):
  q = 0
  i = 0
  j = 0
  boolean =[]
  while k:  
    if int(T[i][0]) == q:
      if cuv[j] == T[i][2]:
        cuv =cuv[:j] + T[i][6] + cuv[j+1:]
        if T[i][8] == 'L':
          j -=1
          if j < 0:
            cuv = '#' + cuv[:]

        if T[i][8] == 'R':
          j +=1
          if j > len(cuv) - 1:
            cuv = cuv[:] + '#'
        
        
        q = int(T[i][4])
        if F[0] != '-':
          if T[i][8] == 'H':
            boolean = 'True'
            return (boolean)
        
          if q == int(listToString(F[0])):
            boolean = 'True'
            return (boolean)
        i = -1
        k -=1

    i +=1  
    if i+1 > nr_tranz:
      i -=1
      
      boolean = 'False'
      return (boolean)

if __name__ == "__main__":
  import sys
  #stochez intr-o variabila ce vreau sa citesc de la stdin
  A = sys.stdin.read()
  #stochez intr-un tuplu reprezentarea interna a masinii
  T = readTM(A)
  w = []
  # w este o lista formata din cuvintele introduse
  w = T[1].split()
  #n este numarul de cuvinte
  n = len(w)
  nr_tranz = T[5]
  i = 0

  #in functie de ce e scris pe primul rand la stdin
  #apelez urmatoarele functii

  if T[0] == 'step':
    for i in range(n):
      cuv = w[i].split(',')
      u = cuv[0][1:]
      q = cuv[1] 
      v = cuv[2][:-1]
      w[i] = step(u, q, v, T[3], nr_tranz)
      if w[i] != 'False':
        w[i] = '(' + w[i][0] + ',' + w[i][1] + ',' + w[i][2] + ')'
    print(listToString(w))
  
  if T[0] == 'accept':
    for i in range(n):
      cuv = w[i]
      w[i] = accept( T[4], T[3], nr_tranz, cuv)
    print(listToString(w))

  if T[0] == 'k_accept':
    for i in range(n):
      cuv_k = w[i].split(',')
      cuv = cuv_k[0]
      k = int(cuv_k[1])
      w[i] = k_accept(k, T[4], T[3], nr_tranz, cuv)
      if w[i] == None:
        w[i] = str(False)
    print(listToString(w))