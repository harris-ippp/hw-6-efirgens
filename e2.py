from bs4 import BeautifulSoup
import sys
import requests

election_id = []
election_years = []

for line in open("ELECTION_ID"):
    codes = line.split()[-1]
    full_url = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/".format(codes)
    req = requests.get(full_url)
    soup = BeautifulSoup(req.text, 'html.parser')
    soup = str(soup)

    year = line.split()[0]
    file_name = year + ".csv"
    with open(file_name, "w") as out:
        out.write(soup)
