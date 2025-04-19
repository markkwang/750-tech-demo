import requests
from bs4 import BeautifulSoup

def extract_text_from_url_all(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    text = soup.get_text(separator="\n")
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines[:1000])

def extract_text_from_url_customised(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")
    
    list_of_quotes_and_authors = []

    for quote, author in zip(quotes, authors):
        quote_text = quote.get_text()
        author_text = author.get_text()
        sentence = f"{quote_text} ---- {author_text}"
        list_of_quotes_and_authors.append(sentence)
    return list_of_quotes_and_authors

example_account_payload = {
        "username": "tomsmith",
        "password": "SuperSecretPassword!"
    }

def extract_text_from_url_login(url, secure_url):
    
    request1 = requests.post(url, data=example_account_payload)

    request2 = requests.get(secure_url)

    map = {
        "request1": request1.text,
        "request2": request2.text
    }
    return map

def extract_text_from_url_session(url, secure_url):

    request1 = requests.post(url, data=example_account_payload)

    with requests.Session() as session:
        session.post(url, data=example_account_payload)
        request2 = session.get(secure_url)
        map = {
            "request1": request1.text,
            "request2": request2.text
        }
        return map


