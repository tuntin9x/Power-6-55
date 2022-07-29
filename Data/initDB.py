# Loading craw web database 6-55
# URL https://xoso.me/kqxs-power-6-55-ket-qua-xo-so-power-6-55-vietlott-ngay-hom-nay/109.html
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

date_power655 = list()
power655_data_string = list()
strbase = "https://xoso.me/kqxs-power-6-55-ket-qua-xo-so-power-6-55-vietlott-ngay-hom-nay/"
for i in range (1,110):
    time.sleep(1)
    print(str(i)+".html")
    response = requests.get(strbase+str(i)+".html")
    soup = BeautifulSoup(response.content, "html.parser")
    html_power655_mega645 = soup.findAll(class_='power655 mega645')
    for index in range (0,len(html_power655_mega645)):
        date = html_power655_mega645[index].find('h2',class_='tit-mien clearfix').find('strong')
        temp_date = date.text.split(" ")
        string_date = temp_date[len(temp_date)-2]
        date_power655.append(string_date)
        table = html_power655_mega645[index].find('table',class_='data')
        
        string_power655_line = ""
        power655=list()
        for row in table.findAll("td"):
            power655.append(row)
        for i in range (0,6):
            string_power655_line = string_power655_line + power655[i].text + "-"
        string_power655_line = string_power655_line + power655[6].text
        power655_data_string.append(string_power655_line)
    #print(date_power655[0]+" : ",power655_data_string[0])
date_power655.reverse()
power655_data_string.reverse()
dataFrame = {'Date':date_power655,'Power655':power655_data_string}
#print(dataFrame)
column_names = ['Date', 'Power655']
df = pd.DataFrame(dataFrame)
df.to_csv ('export_data_new.csv', sep=',', encoding='utf-8', header=True, index=False,columns=column_names)
print("Done!")