import requests
from bs4 import BeautifulSoup as bs

github_user = input('Input GitHub Username: ')
url = 'https://github.com/' +github_user
r = requests.get(url)
soup = bs(r.content, 'html.parser')

profile_img = soup.find('img', {'alt': 'Avatar'})['src']
achmnt_img = soup.find('img', {'data-hovercard-type': 'achievement'})['src']
achmnt1_img = soup.find('img', {'data-hovercard-type': 'achievement'})['src']


print(profile_img)
print(achmnt_img)
print(achmnt1_img)

