from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://stepik.org/media/attachments/lesson/209723/3.html"

html = urlopen(url).read().decode("utf-8")
s = str(html)
soup = BeautifulSoup(s, "html.parser")

tds = soup.find_all("td")

numbers = [int(i.string) for i in tds]

print(sum(numbers))
