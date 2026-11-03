print("B1")
from enum_ import citeste_linii
def cai(fisier):
    # TODO: intoarce MULTIMEA cailor din fisier (foloseste citeste_linii din enum)
    return set(citeste_linii(fisier))
baza = cai("baza_suid.txt")
acum = cai("suid.txt")
print("baza:", len(baza), " acum:", len(acum))

print("\nB2")
noi = acum - baza
print(len(noi), "SUID noi fata de sistemul curat")
for c in sorted(noi):
    print(" ", c)

print("\nB3")
from enum_ import nume, GTFO
 
risc = {nume(c): ("mare" if nume(c) in GTFO else "normal") for c in noi}
periculoase = [c for c in sorted(noi) if nume(c) in GTFO]
print("periculoase NOI:", periculoase)
   
