__author__ = 'ivanivanov'
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
resp = requests.get('https://ballotpedia.org/Lisa_Murkowski')
txt = resp.text
soup = BeautifulSoup(txt, 'lxml')

list_of_footnotes = soup.find_all("div", {"class":"widget-value"})
number_of_footnotes = len(soup.find_all("div", {"class":"widget-value"}))
list_of_footnotes2 = soup.find_all("div", {"class":"widget-key"})
number_of_footnotes2 = len(soup.find_all("div", {"class":"widget-key"}))
list_of_footnotes3 = soup.find_all("div", {"class":"widget-row value-only Republican Party"})
number_of_footnotes3 = len(soup.find_all("div", {"class":"widget-row value-only Republican Party"}))

Profession = list_of_footnotes[number_of_footnotes - 1].get_text()
Net_Salary = list_of_footnotes[number_of_footnotes - 6].get_text()
University1 = list_of_footnotes[number_of_footnotes - 11].get_text()
Degree1 = list_of_footnotes2[number_of_footnotes2 - 11].get_text()
Name = soup.find("div", {"class":"widget-row"}).get_text()
Salary = soup.find("div", {"class":"widget-value"}).get_text()
State_House = list_of_footnotes3[number_of_footnotes3 - 7].get_text()
outfile =  open('/Users/ivanivanov/Desktop/bla/bla.txt', 'w')
outfile.write(Name + Salary + Profession + Net_Salary + University1 + Degree1 + State_House)
print(Name)
print(Profession)
print(Salary)
print(Net_Salary)
print(University1)
print(Degree1)
print(State_House)


