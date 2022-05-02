annee = int (input("Entrez l anne a verifier"))

if(annee%4== 0 and annee%100!=0 or annee%400==0):
 print("l annee est une annee bissextile!")
else:
 print("l anne nest pas bissextile")