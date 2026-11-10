# Laborator: funcții, metode și importuri pe web
# Student: Vizir Maximilian
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde

import time
#Exercitiul 9
print("\nExercitiul 9")
import requests
page9 = requests.get(BASE_URL, timeout=TIMEOUT)
print("Status_code " , page9.status_code)
print("Is OK? " , page9.ok)
print("URL: " , page9.url)
print("Codarea: " , page9.encoding)

     # toate acesteasunt atribute, deoarece returneaza o informatie despre pagina noastra, se cheama fara paranteze rotunde

#Exercitiul 10
print("\nExercitiul 10")
try:
    time.sleep(1)
    page10 = requests.get(ECHO_URL + "/this-page-does-not-exist-so-do-you", timeout=TIMEOUT)
    page10.raise_for_status()
except requests.HTTPError:
    print("Pagina care ati incercat-o nu exista")

     #in cazul dat BASE_URL + string-ul oricum ne returneaza succes, de aceea am incercat cu ECHO_URL
     #pentru ca sa-mi afiseze print-ul din exceptie

#Exercitiul 11
print("\nExercitiul 11")
for c,k in page9.headers.items():
    print(c + " : " + k)

#Exercitiul 12
print("\nExercitiul 12")
#page12 = requests.get(BASE_URL, timeout=TIMEOUT)
print(page9.headers.get("Server", "lipseste"))
print(page9.headers.get("Content-Type", "lipseste"))
print(page9.headers.get("content-type"))
     #aici ori Content-Type ori content-type, ne returneaza aceeasi valoare, deoarece nu este case-sensitive
     #iar lipseste nu se afiseaza, deoarece valorile server si content-type sunt gasite

# Exercitiul 13
print("\nExercitiul 13")
#page13 = requests.get(BASE_URL, timeout=TIMEOUT)
print(page9.text.lower().count("cyber"))

     #putem sa le inlantuim deoarece lower() returneaza un sir, si deja asupra acestui sir chemam count()

#Exercitiul 14
print("\nExercitiul 14")
#page14 = requests.get(BASE_URL, timeout=TIMEOUT)
start = page9.text.find("<title>") + len("<title>")
end = page9.text.find("</title>")
print(page9.text[start:end].strip())

#Exercitiul 15
print("\nExercitiul 15")
#page15 = requests.get(BASE_URL, timeout=TIMEOUT)
lines = page9.text.splitlines()
print(len(lines))
print(len(max(lines, key=len)))

#Exercitiul 16
print("\nExercitiul 16")
startwith = page9.url.startswith(("https"))
if startwith:
    print("Conexiune securizata")
else:
    print("Conexiune nesecurizata")

time.sleep(1)
#Exercitiul 17
print("\nExercitiul 17")
page17 = requests.get("http://cybercor.org", timeout=TIMEOUT)
for res in page17.history:
     print("URL initial",res.url)
     print("Codul de stare: ",res.status_code)
print("URL final: ",page17.url, "\nCodul de stare: ",page17.status_code)

time.sleep(1)
#Exercitiul 18
print("\nExercitiul 1")
page18_get = requests.get(BASE_URL, timeout=TIMEOUT)
time.sleep(1)
page18_head = requests.head(BASE_URL, timeout=TIMEOUT)
print(len(page18_get.content))
print(len(page18_head.content))
     
     #la executare, lungimea la get este de 1540, dar la head este 0, deoarece cu get primesti si corpul la html
     #dar cu head primesti doar niste date, care le afisezi cu .status_code sau .headers

#Exercitiul 19
print("\nExercitiul 19")
if len(page9.cookies) == 0:
     print("Nici un cookie gasit")
else:
     for c in page9.cookies:
          print(c.name)
          print(c.secure)

#Exercitiul 20
print("\nExercitiul 20")
sesiune = requests.Session()
sesiune.headers.update({"User-Agent": "WebLab-Numele Meu"})
time.sleep(1)
page20 = sesiune.get(ECHO_URL +"/headers", timeout=TIMEOUT)
print(page20.json()["headers"]["User-Agent"])
