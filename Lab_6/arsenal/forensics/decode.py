print("\nA1")
s = "Salut"
b = s.encode()          # bytes
print("bytes: ",b, b[0])          # b"Salut" 83
# TODO: tipareste b.hex() si refa bytes din hex
#       cu bytes.fromhex(…)
b = b.hex() 
print("hex: ", b) 
b = bytes.fromhex(b) 
print("bytes: ",b)

pentru_raport = []
#Exercitiul 2
import re
def ghici_strat(s):
    # TODO: daca are %xx -> "url"
    if re.search(r"%[0-9A-Fa-f]{2}", s):
        return "url"
    # TODO: daca doar 0-9 a-f si lungime para -> "hex"
    if len(s) % 2 == 0 and re.fullmatch(r"[0-9a-fA-F]+", s):
        return "hex"
    # TODO: daca doar A-Za-z0-9+/= -> "base64"
    if re.fullmatch(r"[A-Za-z0-9+/]+={0,2}", s):
        return "base64"
    return "necunoscut"
print("A2")
print(ghici_strat("%2Fetc"))   # url
print(ghici_strat("48656c6c6f"))  # hex

#Exercitiul 3
import base64
from urllib.parse import unquote
def desfa(s):
    strat = ghici_strat(s)
    # TODO: pentru fiecare strat, decodeaza
    #   base64 -> base64.b64decode(s)
    if (strat == "base64"):
        return (strat, base64.b64decode(s))
    #hex    -> bytes.fromhex(s)
    if (strat == "hex"):
        return (strat, bytes.fromhex(s))
    #url    -> unquote(s).encode()
    if (strat == "url"):
        return (strat, unquote(s).encode())
print("\nA3")
print(desfa("%2Fetc"))
print(desfa("48656c6c6f"))

print("\nA4")
def citibil(b):
    # TODO: True daca toti octetii sunt 32..126
    return all(32<= c <= 126 for c in b)
 
val = "NTM1OTU3NTk="
for _ in range(8):
    strat, b = desfa(val)
    # TODO: daca citibil(b): opreste si tipareste
    #       altfel val = b.decode(); continua
    if not citibil(b):
        print(val)
        pentru_raport.append(val)
        break
    val = b.decode()

print("\nA5")
date = open("probe/xor.bin", "rb").read()
for k in range(256):
    clar = bytes(b ^ k for b in date)
    # TODO: daca citibil(clar):
    #       print("cheie:", k, clar.decode())
    if citibil(clar):
        print("cheie:",k, clar.decode())
        pentru_raport.append(k)
        break
        

print("\nA6")
import hashlib
for linie in open("probe/hashuri.txt"):
    tinta = linie.strip()
    print(len(tinta))   # 32 md5 / 40 sha1 / 64 sha256
    for cuv in open("probe/wordlist.txt", encoding="latin1"):
        cuv = cuv.strip()
        # TODO: daca hashlib.md5(cuv.encode()).hexdigest()
        #       == tinta: print("gasit:", cuv); break
        if len(tinta) == 32:
            h = hashlib.md5(cuv.encode()).hexdigest()
        elif len(tinta) == 40:
            h = hashlib.sha1(cuv.encode()).hexdigest()
        elif len(tinta) == 64:
            h = hashlib.sha256(cuv.encode()).hexdigest()
        else:
            continue
        if h == tinta:
            print("gasit:", cuv)
            pentru_raport.append(cuv)

print("\nA7")
import argparse, json
p = argparse.ArgumentParser()
p.add_argument("intrare")          # sir sau cale
p.add_argument("--fisier", action="store_true")
a = p.parse_args()
print(a.fisier)
# daca incerc sa printez a.fisier, cand ii dau doar argumentul obligatoriu, "intrare",
# imi afiseaza false, daca prin --fisier, imi returneaza true
rezultate=[]
def text(b):
    try:
        return b.decode()
    except UnicodeDecodeError:
        return b.hex()
if a.fisier:
    for linie in open(a.intrare, "rb"):
        data = linie.strip()
        temp = desfa(data.decode())
        rezultate.append({temp[0]: text(temp[1])})         
else:
    strat, rezultat = "binar", a.intrare
    rezultate.append({strat : rezultat})
with open("fisa.json", "w") as f:
    for r in rezultate:
        json.dump(r,f,indent=2)
print(json.dumps(rezultate, indent=2))

with open("raport.md", "w") as file:
    file.write(f"mesajul ascuns:{pentru_raport[0]}")
    file.write(f"\ncheia: {pentru_raport[1]}")
    file.write("\nparole:\n")
    for c in pentru_raport[2:]:
        file.write(f"{c} \n")

