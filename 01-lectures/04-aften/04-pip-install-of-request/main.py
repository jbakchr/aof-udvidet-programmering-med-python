import requests
from bs4 import BeautifulSoup

r = requests.get("https://bold.dk/fodbold/stillinger/premier-league")

soup = BeautifulSoup(r.text, "html.parser")

table = soup.find_all("table")[0]

table_body = table.find("tbody")

premier_league_leader = table_body.find("tr")

td = premier_league_leader.find_all("td")[0]

href = td.find("a")

print(f"The current Premier League leaders are: {href.span['title']}")
