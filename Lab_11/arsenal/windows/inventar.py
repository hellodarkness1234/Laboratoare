from dataclasses import dataclass, asdict
import json
 
@dataclass
class Proces:
    pid: int
    nume: str
    user: str
    cale: str
    def e_suspect(self):
        for c in CAI_SUSPECTE:
            if c in self.cale:
                return True
        return False

if __name__ == "__main__":
    print("A1")
    p = Proces(3120, "update.exe", "ana", r"C:\Users\ana\AppData\Local\Temp\update.exe")
    print(p.pid, p.nume)
    print(p)

CAI_SUSPECTE = ("\\Temp\\", "\\Roaming\\") 

if __name__ == "__main__":
    print("\nA2")
    print(p.e_suspect()) 

SUSPECTE_ID = {4625, 1102, 7045}
 
@dataclass
class Eveniment:
    id: int; nivel: str; sursa: str; cont: str; mesaj: str
    def e_suspect(self):
        return self.id in SUSPECTE_ID or self.nivel == "critical"

def procese_din_json(cale):
    with open(cale, encoding="utf-8") as f:
        return [Proces(**d) for d in json.load(f)]

if __name__ == "__main__":
    print("\nA4")
    procese = procese_din_json("../../start/start/procese.json")
    print("procese:", len(procese))
    print("suspecte:", sum(1 for p in procese if p.e_suspect()))


print("\nB1")
@dataclass
class Inventar:
    procese: list
    @classmethod
    def din_json(cls,cale):
        with open(cale, encoding="utf-8") as f:
            return cls([Proces(**d) for d in json.load(f)])
    def __len__(self):
        return len(self.procese)
    
    def suspecte(self):
        # TODO: lista proceselor cu p.e_suspect()
        return [s for s in self.procese if s.e_suspect()]
    def pe_user(self):
        # TODO: dict user -> lista de nume (foloseste setdefault)
        rezultat = {}
        for p in self.procese:
            rezultat.setdefault(p.user, []).append(p.nume)
        return rezultat
if __name__ == "__main__":
    inv = Inventar.din_json("../../start/start/procese.json")
    print("procese:", len(inv))
    print("\nB2")
    print(inv.suspecte())
    print(inv.pe_user())

def evenimente_din_json(cale):
    with open(cale, encoding="utf-8") as f:
        return [Eveniment(**d) for d in json.load(f)]

def main():
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("capturi")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()
    inv = Inventar.din_json(a.capturi + "/procese.json")
    ev = evenimente_din_json(a.capturi + "/evenimente.json")
    alarma = [e for e in ev if e.e_suspect()]
    if a.json:
        output = {
            "alarma": [asdict(e) for e in alarma],
            "procese_suspecte": [asdict(p) for p in inv.suspecte()]
        }
        print(json.dumps(output, indent=4))
    else:
        procese_suspecte = inv.suspecte()
        print(f"Procese: {len(inv)} | suspecte: {len(procese_suspecte)}")
        for p in procese_suspecte:
            print(f"  [{p.pid}] {p.nume}  ({p.user})  {p.cale}")
            
        # Afișare secțiune Evenimente
        print(f"Evenimente: {len(ev)} | alarma: {len(alarma)}")
        for e in alarma:
            print(f"  {e.id} [{e.nivel}] {e.cont}: {e.mesaj}")

if __name__=="__main__":
    print("\nB3")
    main()
