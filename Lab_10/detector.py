import parse_auth, argparse,json
from collections import Counter
def try_suspecti(counts, prag):
    if prag < 1:
        raise ValueError(f"prag invalid: {prag} (cel putin 1)")
    # TODO: intoarce lista de (ip, n) cu n >= prag,
    #       sortata descrescator dupa n
    return sorted(((ip,n) for ip, n in counts.items() if n>=prag), key = lambda x:x[1], reverse=True)

def suspecti(counts, prag=10):
    try:
        return try_suspecti(counts, prag)
    except ValueError:
        print("Prag nu poate fi mai mic ca 1")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("log")
    p.add_argument("--prag", type=int, default=10)
    p.add_argument("--json", action="store_true")
    a = p.parse_args()
    esecuri = parse_auth.citeste_esecuri(a.log)
    counts = Counter(e["ip"] for e in esecuri)
    sus = suspecti(counts, a.prag)
    # TODO: cu --json, scoate json.dumps cu {esecuri, pe_ip, suspecti};
    #       fara, un rezumat cu "BRUTE FORCE" pe fiecare suspect
    if a.json:
        print(json.dumps({"esecuri":len(esecuri),"pe_ip":dict(counts),"suspecti": [{"ip":ip,"n":n} for ip,n in sus]}))
    else:
        print(f"Total esecuri:{len(esecuri)}")
        print(f"IP-uri distincte: {len(counts)}")
        if sus:
            for ip,n in sus:
                print(f"BRUTE FORCE: {ip} ({n} esecuri)")
        else:
            print(f"Nici un suspect pentru prag>={a.prag}")

if __name__ == "__main__":
    print("B1")
    c = Counter({"203.0.113.9": 13, "198.51.100.7": 2})
    print(suspecti(c))
    print(suspecti(c, prag=2))
   
    print("\nB3")
    main()

    
