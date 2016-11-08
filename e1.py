from bs4 import BeautifulSoup
import sys
import requests

office_id = {"President" : 1, "Senator" : 6, "Representative" : 5}
search_site = "http://historical.elections.virginia.gov/elections/search/show_details:1/office_id:{}/stage:{}"
download_site = "http://historical.elections.virginia.gov/elections/download{}/precincts_include:0/"
full_url = search_site.format(office_id['President'], 'General')

req = requests.get(full_url)
soup = BeautifulSoup(req.text, 'lxml')

soup.find('tr', 'election_item') #find individual one
soup.find_all('tr') #bring up all of them

len(soup.find_all("tr", "election_item"))

#id = election['id'].split('-')[-1]
#print(id)
election_id = []
election_years = []
for election in soup.find_all('tr', 'election_item'):
    eid = election['id'].split('-')[-1]
    election_id.append(eid)
    year = election.find('td', 'year first').text
    election_years.append(year)
print(election_id)
print(election_years)
#e.find('td', 'year first').text #(or .string would work)

#opening and closing files
# 'w' = write 'r' = read and 'a' = append -- use to tell python what you want to do with a file
with open("ELECTION_ID", 'w') as f:
    for i in range (len(election_id)):
        line = " ".join([election_years[i], election_id[i]])
        f.write(line+"\n")
