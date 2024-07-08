from bs4 import BeautifulSoup
import requests



ponzi = requests.get('https://blk68.com/')
print(ponzi.status_code)


# soup = BeautifulSoup(ponzi)
# print(soup.prettyfy())