
from Pro_princ_final import * 
import time

start = time.time()


cdr1 = Cdr("Text_algo(information).txt")
cdr1._Open()
facture1 = Facture(cdr1.resultat)
facture1.Definition()


statistique1 = Statistique(cdr1.resultat)
statistique1.stat()



print(time.time() - start)

# temps d'éxecution réel l est égal à 1 ms
# La complexité est de O(n²) car notre algorithme exploite les boucles imbriquées
