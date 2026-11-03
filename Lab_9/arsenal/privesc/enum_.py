import argparse, json, os
def citeste_linii(cale):
    with open(cale, encoding="utf-8") as f:
        linii = [l.strip() for l in f if not l.strip().startswith('#') and l.strip()]
    return linii

def nume(cale):
    # TODO: intoarce ce e dupa ultimul "/"  (vezi rsplit)
    temp = cale.rsplit("/")
    return temp[-1]

def suid_constatari(cale):
    cai = citeste_linii(cale)
    cai_set = sorted(set(cai))
    # TODO: pentru fiecare cale UNICA, in ordine sortata, un dict:
    #   {"cale": c, "nume": nume(c),
    #    "risc": "mare" daca nume(c) in GTFO, altfel "normal"}
    lista = [{"cale":c, "nume":nume(c),"risc": "mare" if nume(c) in GTFO else "mic"} for c in cai_set]
    return lista

def sudo_constatari(cale):
    out = []
    for ln in citeste_linii(cale):
        user, drept = ln.split(" : ", 1)                          
        # TODO: adauga {"user": user.strip(), "drept": drept.strip(),
        #   "risc": "mare" daca "NOPASSWD" in drept, altfel "normal"}
        out.append({"user":user.strip(),"drept":drept.strip(),"risc":"mare" if "NOPASSWD" in drept else "normal"})
    return out
 
def cron_constatari(cale):
    out = []
    # TODO: campuri = ln.split(); user = campuri[5];
    #   comanda = " ".join(campuri[6:]); dict cu user si comanda
    for ln in citeste_linii(cale):
        campuri = ln.split()
        user = campuri[5]
        comanda = " ".join(campuri[6:])
        out.append({"user":user,"comanda":comanda,"risc":"mare" if user == "root" else "normal"})
    return out

def enumereaza(d):
    return {
        "suid": suid_constatari(os.path.join(d, "suid.txt")),
        "sudo": sudo_constatari(os.path.join(d, "sudo.txt")),
        "cron": cron_constatari(os.path.join(d, "crontab.txt")),
    }

def main():
    p = argparse.ArgumentParser()
    p.add_argument("capturi")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()
    raport = enumereaza(a.capturi)
    if a.json:
        print(json.dumps(raport, indent=2, ensure_ascii=False)); return
    for categorie, lista in raport.items():
        mari = [c for c in lista if c.get("risc") == "mare"]
        print(f"{categorie}: {len(lista)} gasite, {len(mari)} cu risc mare")
    # TODO: utilizatorii implicati = multimea userilor din sudo REUNITA cu cei din cron
    useri_sudo = {d["user"] for d in raport["sudo"]}
    useri_cron = {d["user"] for d in raport["cron"]}
    utilizatori_implicati = useri_sudo | useri_cron
    print("utilizatori implicati:", utilizatori_implicati)
    with open("enum.json", "w", encoding="utf-8") as f:
        json.dump(raport, f, indent=2, ensure_ascii=False)
    print("Raport salvat in enum.json")

GTFO = {"find", "vim.basic", "vim", "nmap", "cp", "bash",
            "less", "awk", "python3", "perl"}

if __name__ == "__main__":
    print("A1")
    cai = citeste_linii("suid.txt")
    print("linii SUID:", len(cai))

    print("\nA2")
    nume_unice = {nume(c) for c in cai}
    print("SUID distincte:", len(nume_unice))
    
    print("\nA3")

    suid = suid_constatari("suid.txt")
    mari = [c for c in suid if c["risc"] == "mare"]
    print(len(suid), "SUID,", len(mari), "cu risc mare")
    print(sorted(c["nume"] for c in mari))

    print("\nA4")
    print(enumereaza(""))

    print("\nA5")
    main()
