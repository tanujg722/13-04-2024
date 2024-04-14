import requests
import bs4
from bs4 import BeautifulSoup
#result = requests.get("http://www.example.com")
#print(type(result))
#print(result.text) # prettify
#print(result.content) # here we unstructured text

#soup = BeautifulSoup(result.text,"lxml")
#print(soup)
#print(soup.select("title"))
#print(soup.select('p')) # here we para
#print(soup.select('h1'))
#print(result.status_code)
#print(soup.select('a')) # first anchor tag

# tag
#tag = soup.html
#print(tag)
#print(type(tag))
#print(soup.a)
#print(soup.h1)

# Navigablestring
#print(soup.p.string)
#print(soup.a.string)
#print(soup.h1.string)

#beautifulsoup
#print(soup.body)
#print(soup.head)
#print(soup.find("p"))
#print(soup.find_all("p"))

#Comment
#com = soup.p.string
#print(com)

web = requests.get("http://www.tutorialsfreak.com/")
#print(web)
#print(web.content)
soup = BeautifulSoup(web.content,"lxml")
#print(soup.prettify())
#print(soup.find_all("p")) # we get all paragraph tag
#print(soup.find_all("p3"))
#print(soup.find_all("h3"))

# find element by class
#class_data = soup.find("div",class_ = "app-container")
#print(class_data)
#class_data.find_all("p")


id_data = soup.find("div",id ="app-fronted")
id_data.find_all("p")