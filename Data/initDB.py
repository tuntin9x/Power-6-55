# Loading craw web database 6-55
# URL https://xoso.me/kqxs-power-6-55-ket-qua-xo-so-power-6-55-vietlott-ngay-hom-nay/109.html
import requests
from bs4 import BeautifulSoup

strbase = "https://xoso.me/kqxs-power-6-55-ket-qua-xo-so-power-6-55-vietlott-ngay-hom-nay/"
response = requests.get(strbase+"109.html")
soup = BeautifulSoup(response.content, "html.parser")
html_power655_mega645 = soup.findAll(class_='power655 mega645')
date = html_power655_mega645[0].find('h2',class_='tit-mien clearfix').find('strong')
#print(date.text)
table = html_power655_mega645[0].find('table',class_='data')
string_kqsx = ""
rows=list()
for row in table.findAll("td"):
   rows.append(row)
for i in range (0,6):
    string_kqsx = string_kqsx + rows[i].text + "-"
string_kqsx = string_kqsx + rows[6].text
print(string_kqsx)