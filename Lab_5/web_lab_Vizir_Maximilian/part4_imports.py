# Laborator: funcții, metode și importuri pe web
# Student: Vizir Maximilian

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde

import time, requests, urllib, re

#Exercitiul 35
print("\nExercitiul 35")
def urlparser(url):
      parsed = urllib.parse.urlparse(url)
      print(parsed.scheme)
      print(parsed.netloc)
      print(parsed.path)
      print(parsed.query)
      print(parsed.fragment)
print(urlparser("https://cybercor.org/path?x=1#top"))

#Exercitiul 36
print("\nExercitiul 36")
def urljoiner(url):
      pagini = ["/about", "contact.html", "../index.html"]
      url_compus = []
      for p in pagini:
            url_compus.append(urllib.parse.urljoin(url,p))
      return url_compus
print(urljoiner(BASE_URL))

#Exercitiul 37
print("\nExercitiul 37")
def extract_links(html):
      response = requests.get(html, timeout=TIMEOUT)
      links = re.findall(r'href="([^"]+)"', response.text)
      links_not_repeated = []
      for l in links:
            if (l not in links_not_repeated):
                  links_not_repeated.append(l)
      return links_not_repeated
time.sleep(1)
print(extract_links(BASE_URL))

#Exercitiul 38
print("\nExercitiul 38")
def split_links(links, domain):
      same = []
      different = []
      for l in links:
            full = urllib.parse.urljoin("https://"+domain,l)
            if(urllib.parse.urlparse(full).netloc == domain):
                  same.append(full)
            else:
                  different.append(full)
      return same, different
time.sleep(1)
print(split_links(extract_links(BASE_URL), urllib.parse.urlparse(BASE_URL).netloc))

#Exercitiul 39
print("\nExercitiul 39")
from html.parser import HTMLParser
 
class ImageFinder(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
 
    def handle_starttag(self, tag, attrs):
        if(tag == "img"):
              for attr in attrs:
                    if(attr[0] == "src"):
                          self.images.append(attr[1])
test_html = """
<html><body>
  <img src="/logo.png" alt="Logo">
  <IMG SRC="poza.jpg">
  <img alt="imagine fără src">
  <img src="https://cdn.example.com/banner.webp" />
  <a href="/despre">Aceasta nu este o imagine</a>
</body></html>
"""

finder = ImageFinder()
finder.feed(test_html)
print(finder.images)
 
assert finder.images == [
    "/logo.png",                            # imagine obișnuită
    "poza.jpg",                             # tag scris cu majuscule
    "https://cdn.example.com/banner.webp",  # tag care se închide singur
], "Parserul nu a găsit exact imaginile așteptate"
print("Testul a trecut!") 

print("\nIar acum pe pagina reala")
time.sleep(1)
page39 = requests.get(BASE_URL, timeout=TIMEOUT)
finder_real = ImageFinder()
finder_real.feed(page39.text)
print("verificare prin finder_real.images: ",len(finder_real.images), "imagini gasite")
for src in finder_real.images:
      print(src)
print("verificare prin count: ", page39.text.lower().count("<img"))

#Exercitiul 40
print("\nExercitiul 40")
import hashlib
def page_fingerprint(url):
      response = requests.get(url, timeout=TIMEOUT)
      return hashlib.sha256(response.content).hexdigest()
time.sleep(1)
print(page_fingerprint(BASE_URL))
time.sleep(1)
print(page_fingerprint(BASE_URL))

      #s-ar schimba hash-ul in cazul in care codul html s-ar schimba macar putin (un caracter)
      #s-au cand pagina are ceva dinamic,vreun contor sau ceva. atunci la fiecare instalare a paginii
      #pot fi valori diferite, de aici si hash diferit.

#Exercitiul 41
print("\nExercitiul 41")
import json
with open("headers.json", "w") as file:
      json.dump(dict(page39.headers), file, indent=2)

with open("headers.json", "r") as file:
      headers = json.load(file)
print(headers.get("Server"))


#Exercitiul 42
print("\nExercitiul 42")
import socket
def resolve(hostname):
      return socket.gethostbyname(hostname)
print(resolve(urllib.parse.urlparse(BASE_URL).netloc))

#Exercitiul 43
print("\nExercitiul 43")
import ssl, socket
def cert_days_left(hostname):
      context = ssl.create_default_context()
      with socket.create_connection((hostname,443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                  time_string = ssock.getpeercert()["notAfter"]
                  time_int = ssl.cert_time_to_seconds(time_string)
                  return (time_int-time.time())/86400
print(cert_days_left(urllib.parse.urlparse(BASE_URL).netloc))

