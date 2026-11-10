# Laborator: funcții, metode și importuri pe web
# Student: Vizir Maximilian
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde

# Exercitiul 1
import time
print("\nExercitiul 1")
import requests
print(requests.__version__)

import urllib.request
print(urllib.request.__version__)

    # requests necesita pip install, deoarece este un modul care
    # este scris de o alta persoana si publicata, 
    # iar urllib se instaleaza impreuna cu instalarea la python

# Exercitiul 2
print("\nExercitiul 2")
page2 = requests.get(BASE_URL, timeout=TIMEOUT)
print(page2.status_code)
time.sleep(1)
from requests import get
page2_ = get(BASE_URL, timeout=TIMEOUT)
print(page2_.status_code)

    #avantajul la import requests, este ca daca vom avea doua metode cu aceeasi denumire
    #programul va intelege la care ne adresam deoarece le chemam prin .
    #in al doilea caz, chemarea este mai rapida, adresandu-ne doar prin get, dar pot 
    #aparea conflicte daca sunt mai multe metode la fel

# Exercitiul 3
print("\nExercitiul 3")
import requests as rq
time.sleep(1)
page3 = rq.get(BASE_URL, timeout=TIMEOUT)
print(page3.status_code)

    #un alias face codul mai usor atunci cand este importat corect. spre exemplu a fost 
    #decis pe internet sau ca o conventie ca requests sa fie importat ca rq, astfel denumirea
    #e usoara de tinut minte. Dar poate sa faca mai greu de citit, in caz ca ar fi importat ca 
    #niste denumiri aleatorii, spre exemplu import requests as x sau y sau ceva. atunci este mai 
    #greu de citit y.get(...)

# Exercitiul 4
print("\nExercitiul 4")
time.sleep(1)
page4 = urllib.request.urlopen(ECHO_URL)
print(page4.status)
print(page4.read().decode("utf-8")[:200])

    #pagina cyberorg returneaza 403 cand incerci cu urllib.requests sa o descarci

#Exercitiul 5
print("\nExercitiul 5")
print(dir(requests))

     #Requests este o clasa, in genere este o conventie care spune ca clasele se denumesc doar cu litere mari
     #get este o functie, deoarece aceasta ne returneaza o valoare, care este pagina pe care o descarcam
     #status_code este o metoda deoarece iti da codul de stare al paginii dintr-o variabila deja creata

#Exercitiul 6
print("\nExercitiul 6")
help(requests.get)
help(requests.request)

     #in requests.get nu este parametrul necesar timeout, el se gaseste in requests.request, de asemenea
     #a fost folosit in exercitiile anterioare ca argument timeout=TIMEOUT

#Exercitiul 7
print("\nExercitiul 7")
time.sleep(1)
start_time = time.perf_counter()
page7 = requests.get(BASE_URL, timeout=TIMEOUT)
end_time = time.perf_counter()
print(page7.status_code)
print(page7.elapsed)
print(end_time - start_time)

     # la afisarea ambelor timpuri din modulul time si modulul requests, se afiseaza aproximativ acelasi timp
     #diferenta este de milisecunde 

#Exercitiul 8
print("\nExercitiul 8")
try:
    import bs4
except ImportError:
    print("Instalați modulul cu: pip install beautifulsoup4.")

     # aici se afiseaza la rulare print din exceptie, deoarece modulul nu este instalat.
