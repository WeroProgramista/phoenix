import requests
from bs4 import BeautifulSoup


url = 'https://www.ums.gov.pl/ruch_statkow/inbound.php'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print('Statki spodzeiwane Swinoujscie:')
table = soup.find('table', {'id': 'plswi_exp'})
if table:
    rows = table.find_all('tr')

    for row in rows:
        cells = row.find_all('td')
        if len(cells) > 0:
            for cell in cells:
                vessel_name = cells[1].text.strip() 
                agent = cells[3].text.strip()
                eta = cells[4].text.strip()
                status = cells[7].text.strip()
            print(vessel_name, agent, eta, status)
else:
    print('Nie znaleziono tabeli "plswi_exp"')


print('Statki spodzeiwane Szczecin:')
table = soup.find('table', {'id': 'plszz_exp'})
if table:
    rows = table.find_all('tr')

    for row in rows:
        cells = row.find_all('td')
        if len(cells) > 0:
            for cell in cells:
                vessel_name = cells[1].text.strip() 
                agent = cells[3].text.strip()
                eta = cells[4].text.strip()
                status = cells[7].text.strip()
            print(vessel_name, agent, eta, status)
else:
    print('Nie znaleziono tabeli "plszz_exp"')


url = 'https://www.ums.gov.pl/ruch_statkow/port.php'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print('Statki w porcie Swinoujscie:')
table = soup.find('table', {'id': 'plswi_in'})
if table:
    rows = table.find_all('tr')

    for row in rows:
        cells = row.find_all('td')
        if len(cells) > 0:
            for cell in cells:
                vessel_name = cells[1].text.strip() 
                agent = cells[3].text.strip()
                eta = cells[4].text.strip()
                quay = cells[5].text.strip()
            print(vessel_name, agent, eta, quay)
else:
    print('Nie znaleziono tabeli "plswi_in"')

print('Statki w porcie Szczecin:')
table = soup.find('table', {'id': 'plszz_in'})
if table:
    rows = table.find_all('tr')

    for row in rows:
        cells = row.find_all('td')
        if len(cells) > 0:
            for cell in cells:
                vessel_name = cells[1].text.strip() 
                agent = cells[3].text.strip()
                eta = cells[4].text.strip()
                quay = cells[7].text.strip()
            print(vessel_name, agent, eta, quay)
else:
    print('Nie znaleziono tabeli "plszz_in"')
