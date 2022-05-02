import random
def tri_insertion_inv(L):
    N = len(L)
    for n in range(1,N):
        cle = L[n]
        j = n-1
        while j>=0 and L[j] < cle:
            L[j+1] = L[j] 
            j = j-1
        L[j+1] = cle

liste = []
for k in range(10):
    liste.append(random.randint(0,20))
tri_insertion_inv(liste)
                      
print(liste)