import requests, wget, os, shutil
from bs4 import BeautifulSoup
from zipfile import ZipFile

webname = r"https://theweekinchess.com/zips"
sfxname = 'g.zip'

myheaders = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}

url = 'https://theweekinchess.com/twic'

# Find the number of the latest issue:
r = requests.get(url, headers=myheaders)
html_contents = r.text
html_soup = BeautifulSoup(html_contents, 'html.parser')

# Find the first table tag, then the second row, then the first cell:
first_table = html_soup.find('table', {"class":"results-table"})
secondrow = first_table.find('tr', {"class":""})
entry = secondrow.find('td').get_text(strip=True)

# concatenate webpath:
fullpath = os.path.join(webname + r"/twic" + entry + sfxname)

# optional: print fullpath to check results
# print(fullpath)

# download the file, using wget
file_name = wget.download(fullpath)

# move the file to a specific directory (change as required)
shutil.move(file_name, "c:/pgn/twic/new/aaa.zip")

# unzip the file (change the path as required)
with ZipFile("c:/pgn/twic/new/aaa.zip", 'r') as zipObj:
    # Extract the contents of the zip file in directory on C:
    zipObj.extractall(path="c:/pgn/twic/new")

# delete the zip file
os.remove("c:/pgn/twic/new/aaa.zip")

# print success message
print("\n\nLatest TWIC file downloaded, unzipped and saved in the C:/PGN/Twic/NEW folder", "\n")
