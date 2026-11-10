#Laborator: funcții, metode și importuri pe web
# Student: Vizir Maximilian

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde

#Exercitiul 44
import time
print("\nExercitiul 44")
import webtools
print(webtools.get_title(webtools.fetch(BASE_URL)))

#Exercitiul 45
print("\nExercitiul 45")
from webtools import fetch, get_title, security_headers
time.sleep(1)
print(get_title(fetch(BASE_URL)))

      #in caz ca am avea o functie get_title in main.pyб atunci va depinde de ce a fost ultima
      #from ... import ... sau def...() . Daca ultima este importul, atunci scriind get_title
      #se va chema din import, daca functia, atunci se va chema functia


#Exercitiul 47
print("\nExercitiul 47")
print(webtools.DEFAULT_HEADERS)


#Exercitiul 48
print("\nExercitiul 48")
import argparse
parser = argparse.ArgumentParser(description="Hmmm")
parser.add_argument("url", help="adresa site-ului")
args = parser.parse_args()
time.sleep(1)
print(webtools.get_title(webtools.fetch(args.url)))

#Exercitiul 49
print("\nExercitiul 49")
import csv,time
from datetime import datetime
path = ["/", "/robots.txt", "/sitemap.xml"]
check_time = []
status_code = []
for p in path:
      status_code.append(webtools.check_paths(BASE_URL,p))
      check_time.append(datetime.now().isoformat())
      time.sleep(1)
with open("raport.csv", "w", newline="") as file:
      writer = csv.writer(file)
      writer.writerow(["path","status","checked_at"])
      for i in range(3):
            writer.writerow([path[i],status_code[i],check_time[i]])

            
#Exercitiul 50
print("\nExercitiul 50\nScriere in fisier")
time.sleep(1)
webtools.site_report(BASE_URL)



#Exercitiul bonus
from bs4 import BeautifulSoup

def get_title_bs(html):
      soup = BeautifulSoup(html.text, "html.parser")
      if(soup.title is None or soup.title.string is None): return ""
      return soup.title.string.strip()

def extract_links_bs(html):
      soup = BeautifulSoup(html.text, "html.parser")
      links = []
      for tag in soup.find_all(href=True):
            if(tag["href"] not in links):
                  links.append(tag["href"])
      return links
      

      # Cu BeautifulSoup codul e mai scurt (extract_links nu mai are nevoie de re)
      # și mai sigur: find("<title>") și regex-ul href="..." ratează <TITLE lang="ro">,
      # href='...' sau href = "...", pe când BeautifulSoup înțelege structura HTML-ului.
      # Dezavantaj: e o bibliotecă externă, care cere pip install.
