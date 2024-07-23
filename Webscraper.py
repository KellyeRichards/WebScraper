from bs4 import BeautifulSoup
import requests

url = 'https://www.scrapethissite.com/pages/forms/' 
page = requests.get(url)  
soup = BeautifulSoup(page.text, 'html')  
print(soup.prettify())
soup.find('div')
soup.find_all('div')
soup.find_all('div', class_ = 'col-md-12')
soup.find_all('p', class_ = 'lead')  
soup.find('p', class_ = 'lead').text.strip() 
soup.find_all('td')
soup.find_all('th')