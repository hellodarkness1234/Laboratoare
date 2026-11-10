# Laborator: funcții, metode și importuri pe web
# Student: Vizir Maximilian
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde

#Exercitiul 21
import requests, time
print("Exercitiul 21")
def fetch(url):
     response = requests.get(url, timeout=TIMEOUT)
     return response

print(fetch(BASE_URL).status_code)

#Exercitiul 22
print("\nExercitiul 22")
def get_status(url : str) -> int:
     response = requests.get(url, timeout=TIMEOUT)
     return response.status_code
time.sleep(1)
print(get_status(BASE_URL+"/"))
time.sleep(1)
print(get_status(BASE_URL+"/robots.txt"))
time.sleep(1)
print(get_status(BASE_URL+"/itemap.xml"))


#Exercitiul 23
print("\nExercitiul 23")
def fetch_23(url, timeout=10):
      response = requests.get(url, timeout=timeout)
      return response
time.sleep(1)
print(fetch_23(BASE_URL, timeout=3))
time.sleep(1)
print(fetch_23(BASE_URL))

#Exercitiul 24
print("\nExercitiul 24")
def get_title(html):
      """(Exercitiul 25: Returnează titlul paginii dintr-un șir HTML."""
      start = html.text.find("<title>") + len("<title>")
      end = html.text.find("</title>")
      return html.text[start:end].strip()
time.sleep(1)
page24 = requests.get(BASE_URL, timeout=TIMEOUT)
print(get_title(page24))

#Exercitiul 25
print("\nExercitiul 25")
print(help(get_title))

#Exercitiul 26
print("\nExercitiul 26")
try:
      print(get_status(123))
except requests.exceptions.MissingSchema:
      print("Functia get_status primeste ca valoare pagina, nu int")
      
      #adnotarile de tip sunt doar pentru persoana ce citeste codul, de aceea oricum returneaza eroare la chemarea functiei
      #cu int in loc de cea ceruta str

#Exercitiul 27
print("\nExercitiul 27")
def page_exists(url):
      try:
            response = requests.get(url, timeout=TIMEOUT)
            return True
      except requests.RequestException:
            return False
time.sleep(1)
print(page_exists(BASE_URL))

#Exercitiul 28
print("\nExercitiul 28")
path = ["/", "/robots.txt", "/sitemap.xml"]
def check_paths(base, paths):
      status_codes = {}
      for p in paths:
            response = requests.get(base + p, timeout=TIMEOUT)
            status_codes[p] = response.status_code
            time.sleep(1)
      return status_codes
time.sleep(1)
print(check_paths(BASE_URL, path))

#Exercitiul 29
print("\nExercitiul 29")
def get_header(url, name, default="lipseste"):
      response = requests.get(url, timeout=TIMEOUT)
      return response.headers.get(name, default)
print(get_header(BASE_URL, "Server"))

#Exercitiul 30
print("\nExercitiul 30")
def security_headers(url):
      response = requests.get(url, timeout=TIMEOUT)
      exists = {}
      antet = ["Strict-Transport-Security", "Content-Security-Policy", "X-Frame-Options", "X-Content-Type-Options", "Referrer-Policy"]
      for a in antet:
            exists[a] = a in response.headers
      return exists
time.sleep(1)
print(security_headers(BASE_URL))

#Exercitiul 31
print("\nExercitiul 31")
def score_headers(results):
      count = 0
      for k in results.values():
            if(k): count+=1
      return f"{count}/{len(results.values())}"
time.sleep(1)
print(score_headers(security_headers(BASE_URL)))

#Exercitiul 32
print("\nExercitiul 32")
def fetch_robots(base):
      response = requests.get(base+"/robots.txt", timeout=TIMEOUT)
      if(response.status_code == 200): 
            return response.text
      else: return None
def disallowed_paths(robots_text):
      disallowed = []
      if(robots_text is None): return []
      text_lines = robots_text.splitlines()
      for t in text_lines:
            if(t.split(":",1)[0].strip().lower() == "disallow"): 
                  disallowed.append(t.split(":",1)[1].strip()) 
      return disallowed
time.sleep(1)
print(disallowed_paths(fetch_robots(BASE_URL)))
print(disallowed_paths(None))

#Exercitiul 33
print("\nExercitiul 33")
def response_times(*urls):
      times = {}
      for u in urls:
            response = requests.get(u,timeout=TIMEOUT)
            times[u] = response.elapsed.total_seconds()
            time.sleep(1)
      return times
time.sleep(1)
print(response_times(BASE_URL, ECHO_URL))

#Exercitiul 34
print("\nExercitiul 34")
def log(message, **details):
      mesaj = f"{message}"
      for c,k in details.items():
            mesaj += f" | {c}={k}"
      return mesaj
print(log("verificat", url=BASE_URL, status=200))
