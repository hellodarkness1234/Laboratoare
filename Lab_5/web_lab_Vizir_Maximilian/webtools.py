#Exercitiul 44, adaugarea functiilor intr-un fisier .py aparte
TIMEOUT = 10
DEFAULT_HEADERS = {"User-Agent" : "WebLab-<Numele vostru :D>"}
import requests,time,re, json, socket, ssl,urllib.parse

def fetch(url):
      response = requests.get(url, headers=DEFAULT_HEADERS ,timeout=TIMEOUT)
      return response

def get_status(html):
      return html.status_code

def get_title(html):
      start = html.text.find("<title>") + len("<title>")
      end = html.text.find("</title>")
      return html.text[start:end].strip()

def security_headers(html):
    antete = ["Strict-Transport-Security", "Content-Security-Policy",
              "X-Frame-Options", "X-Content-Type-Options", "Referrer-Policy"]
    exists = {}
    for a in antete:
        exists[a] = a in html.headers
    return exists

def check_paths(base, path):
      response = requests.get(base+path, timeout=TIMEOUT)
      return response.status_code

def score_headers(results):
      count = 0
      for k in results.values():
            if(k): count+=1
      return f"{count}/{len(results.values())}"

def resolve(hostname):
      return socket.gethostbyname(hostname)

def cert_days_left(hostname):
      context = ssl.create_default_context()
      with socket.create_connection((hostname,443), timeout=TIMEOUT) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                  time_string = ssock.getpeercert()["notAfter"]
                  time_int = ssl.cert_time_to_seconds(time_string)
                  return int((time_int-time.time())/86400)

def extract_links(html):
      links = re.findall(r'href="([^"]+)"', html.text)
      links_not_repeated = []
      for l in links:
            if (l not in links_not_repeated):
                  links_not_repeated.append(l)
      return links_not_repeated

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

def fetch_robots(base):
      response = requests.get(base+"/robots.txt", headers=DEFAULT_HEADERS, timeout=TIMEOUT)
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

def site_report(url):
      """Colectează informații despre un site și le salvează în report.json."""
      hostname = urllib.parse.urlparse(url).netloc

      page = fetch(url)
      status = get_status(page)
      title = get_title(page)
      score = score_headers(security_headers(page))
      same, different = split_links(extract_links(page), hostname)

      ip = resolve(hostname)
      days_left = cert_days_left(hostname)

      time.sleep(1)
      page_http = fetch("http://" + hostname)
      chain = []
      for res in page_http.history:
            chain.append(f"{res.status_code} -> {res.headers.get('Location')}")

      time.sleep(1)
      disallowed = disallowed_paths(fetch_robots(url))

      report = {
            "url": url,
            "status": status,
            "final_url": page.url,
            "title": title,
            "ip": ip,
            "redirects": chain,
            "security_score": score,
            "cert_days_left": days_left,
            "internal_links": len(same),
            "external_links": len(different),
            "disallowed_paths": disallowed,
      }

      with open("report.json", "w") as file:
            json.dump(report, file, indent=2, ensure_ascii=False)
      return report




#Exercitiul 46
if __name__ == "__main__":
     print("\nExercitiul 46")
     print("Autotest:", get_status(fetch("https://cybercor.org")))

     #autotest ruleaza doar in caz ca o chemam prin python3 webtools.py, nu si prin python3 main.py
     #deoarece python in primul caz ii da valoarea de __main__ la variabila __name__, iar in al doilea
     #caz, ii da valoarea numelui modulului
